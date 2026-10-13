from flask import Flask, request, jsonify
from database import get_db_connection, create_tables

app = Flask(__name__)

# Create database tables
create_tables()


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Record Management API!",
        "endpoints": {
            "GET /students": "View all students",
            "GET /students/<id>": "View a student",
            "POST /students": "Add a student",
            "PUT /students/<id>": "Update a student",
            "DELETE /students/<id>": "Delete a student"
        }
    })


# Add a new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    course = data.get("course")

    if not all([name, email, course]) or age is None:
        return jsonify({
            "error": "Name, email, age and course are required"
        }), 400

    if not all(isinstance(data.get(key), str) and data[key].strip()
               for key in ("name", "email", "course")):
        return jsonify({
            "error": "Name, email and course must be non-empty strings"
        }), 400

    if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    name = name.strip()
    email = email.strip().lower()
    course = course.strip()

    if "@" not in email or "." not in email.split("@")[-1]:
        return jsonify({"error": "Invalid email address"}), 400

    conn = get_db_connection()

    try:
        cursor = conn.execute(
            "INSERT INTO students (name, email, age, course) VALUES (?, ?, ?, ?)",
            (name, email, age, course)
        )
        conn.commit()

        return jsonify({
            "message": "Student added successfully",
            "student_id": cursor.lastrowid
        }), 201

    except Exception as error:
        if "UNIQUE constraint failed" in str(error):
            return jsonify({"error": "Email already exists"}), 409
        app.logger.exception("Could not add student")
        return jsonify({"error": "Could not add student"}), 500

    finally:
        conn.close()


# View all students with search, filtering and pagination
@app.route("/students", methods=["GET"])
def get_students():
    search = request.args.get("search", "").strip()
    course = request.args.get("course", "").strip()

    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))

        if page < 1 or not 1 <= limit <= 100:
            raise ValueError

    except ValueError:
        return jsonify({
            "error": "Page must be positive and limit must be between 1 and 100"
        }), 400

    conditions = []
    params = []

    if search:
        conditions.append("(name LIKE ? OR email LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%"])

    if course:
        conditions.append("course = ?")
        params.append(course)

    sql = "SELECT * FROM students"

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " ORDER BY id ASC LIMIT ? OFFSET ?"
    params.extend([limit, (page - 1) * limit])

    conn = get_db_connection()

    try:
        students = conn.execute(sql, params).fetchall()

        return jsonify({
            "page": page,
            "limit": limit,
            "students": [dict(student) for student in students]
        }), 200

    finally:
        conn.close()


# View one student
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    conn = get_db_connection()

    try:
        student = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        return jsonify(dict(student)), 200

    finally:
        conn.close()


# Update a student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    allowed_fields = {"name", "email", "age", "course"}

    if not data or not set(data).issubset(allowed_fields):
        return jsonify({"error": "Provide valid student fields"}), 400

    conn = get_db_connection()

    try:
        student = conn.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        updated = dict(student)
        updated.update(data)

        for key in ("name", "email", "course"):
            if not isinstance(updated[key], str) or not updated[key].strip():
                return jsonify({"error": f"{key} must be a non-empty string"}), 400
            updated[key] = updated[key].strip()

        updated["email"] = updated["email"].lower()

        if (
            not isinstance(updated["age"], int)
            or isinstance(updated["age"], bool)
            or updated["age"] <= 0
        ):
            return jsonify({"error": "Age must be a positive integer"}), 400

        email = updated["email"]

        if "@" not in email or "." not in email.split("@")[-1]:
            return jsonify({"error": "Invalid email address"}), 400

        conn.execute(
            """
            UPDATE students
            SET name = ?, email = ?, age = ?, course = ?
            WHERE id = ?
            """,
            (
                updated["name"],
                updated["email"],
                updated["age"],
                updated["course"],
                student_id
            )
        )

        conn.commit()

        return jsonify({"message": "Student updated successfully"}), 200

    except Exception as error:
        if "UNIQUE constraint failed" in str(error):
            return jsonify({"error": "Email already exists"}), 409
        app.logger.exception("Could not update student")
        return jsonify({"error": "Could not update student"}), 500

    finally:
        conn.close()


# Delete a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

        conn.commit()

        return jsonify({"message": "Student deleted successfully"}), 200

    finally:
        conn.close()

# ================= COURSES API =================

# Add a new course
@app.route("/courses", methods=["POST"])
def add_course():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    course_name = data.get("course_name")
    description = data.get("description", "")

    if not isinstance(course_name, str) or not course_name.strip():
        return jsonify({"error": "Course name is required"}), 400

    if not isinstance(description, str):
        return jsonify({"error": "Description must be a string"}), 400

    conn = get_db_connection()

    try:
        cursor = conn.execute(
            "INSERT INTO courses (course_name, description) VALUES (?, ?)",
            (course_name.strip(), description.strip())
        )
        conn.commit()

        return jsonify({
            "message": "Course added successfully",
            "course_id": cursor.lastrowid
        }), 201

    except Exception as error:
        if "UNIQUE constraint failed" in str(error):
            return jsonify({"error": "Course already exists"}), 409

        app.logger.exception("Could not add course")
        return jsonify({"error": "Could not add course"}), 500

    finally:
        conn.close()


# View all courses
@app.route("/courses", methods=["GET"])
def get_courses():
    conn = get_db_connection()

    try:
        courses = conn.execute(
            "SELECT * FROM courses ORDER BY id"
        ).fetchall()

        return jsonify({
            "courses": [dict(course) for course in courses]
        }), 200

    finally:
        conn.close()


# View a single course
@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    conn = get_db_connection()

    try:
        course = conn.execute(
            "SELECT * FROM courses WHERE id = ?",
            (course_id,)
        ).fetchone()

        if course is None:
            return jsonify({"error": "Course not found"}), 404

        return jsonify(dict(course)), 200

    finally:
        conn.close()


# Update a course
@app.route("/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    course_name = data.get("course_name")
    description = data.get("description", "")

    if not isinstance(course_name, str) or not course_name.strip():
        return jsonify({"error": "Course name is required"}), 400

    if not isinstance(description, str):
        return jsonify({"error": "Description must be a string"}), 400

    conn = get_db_connection()

    try:
        existing = conn.execute(
            "SELECT id FROM courses WHERE id = ?",
            (course_id,)
        ).fetchone()

        if existing is None:
            return jsonify({"error": "Course not found"}), 404

        conn.execute(
            """
            UPDATE courses
            SET course_name = ?, description = ?
            WHERE id = ?
            """,
            (course_name.strip(), description.strip(), course_id)
        )
        conn.commit()

        return jsonify({"message": "Course updated successfully"}), 200

    except Exception as error:
        if "UNIQUE constraint failed" in str(error):
            return jsonify({"error": "Course already exists"}), 409

        app.logger.exception("Could not update course")
        return jsonify({"error": "Could not update course"}), 500

    finally:
        conn.close()


# Delete a course
@app.route("/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            "DELETE FROM courses WHERE id = ?",
            (course_id,)
        )

        if cursor.rowcount == 0:
            return jsonify({"error": "Course not found"}), 404

        conn.commit()

        return jsonify({"message": "Course deleted successfully"}), 200

    finally:
        conn.close()

        # ================= ENROLLMENTS API =================

# Enroll a student in a course
@app.route("/enrollments", methods=["POST"])
def add_enrollment():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    student_id = data.get("student_id")
    course_id = data.get("course_id")

    if (
        not isinstance(student_id, int)
        or isinstance(student_id, bool)
        or student_id <= 0
        or not isinstance(course_id, int)
        or isinstance(course_id, bool)
        or course_id <= 0
    ):
        return jsonify({
            "error": "Valid student_id and course_id are required"
        }), 400

    conn = get_db_connection()

    try:
        student = conn.execute(
            "SELECT id FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

        if student is None:
            return jsonify({"error": "Student not found"}), 404

        course = conn.execute(
            "SELECT id FROM courses WHERE id = ?",
            (course_id,)
        ).fetchone()

        if course is None:
            return jsonify({"error": "Course not found"}), 404

        cursor = conn.execute(
            """
            INSERT INTO enrollments (student_id, course_id)
            VALUES (?, ?)
            """,
            (student_id, course_id)
        )

        conn.commit()

        return jsonify({
            "message": "Student enrolled successfully",
            "enrollment_id": cursor.lastrowid
        }), 201

    except Exception as error:
        if "UNIQUE constraint failed" in str(error):
            return jsonify({
                "error": "Student is already enrolled in this course"
            }), 409

        app.logger.exception("Could not enroll student")
        return jsonify({"error": "Could not enroll student"}), 500

    finally:
        conn.close()


# View all enrollments
@app.route("/enrollments", methods=["GET"])
def get_enrollments():
    conn = get_db_connection()

    try:
        enrollments = conn.execute("""
            SELECT
                e.id AS enrollment_id,
                s.id AS student_id,
                s.name AS student_name,
                c.id AS course_id,
                c.course_name,
                e.enrollment_date
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            JOIN courses c ON e.course_id = c.id
            ORDER BY e.id
        """).fetchall()

        return jsonify({
            "enrollments": [
                dict(enrollment) for enrollment in enrollments
            ]
        }), 200

    finally:
        conn.close()
if __name__ == "__main__":
    app.run(debug=True)