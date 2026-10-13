# Student Record Management API

A RESTful API developed using Python, Flask, and SQLite to manage student records, courses, and course enrollments.

## Project Overview

This project demonstrates backend development concepts, REST API design, database management, CRUD operations, input validation, and error handling.

## Features

### Student Management
- Add new students.
- Retrieve all students.
- Retrieve a student by ID.
- Update student information.
- Delete student records.
- Prevent duplicate email addresses.

### Course Management
- Add new courses.
- Retrieve all courses.
- Retrieve a course by ID.
- Update course information.
- Delete courses.
- Prevent duplicate course names.

### Enrollment Management
- Enroll students in courses.
- Retrieve all enrollment records.
- Validate student and course IDs.
- Prevent duplicate enrollments.
- Maintain relationships using foreign keys.

### Additional Features
- Search students by name or email.
- Filter students by course.
- Paginate student records.
- Validate incoming JSON data.
- Handle API errors using HTTP status codes.
- Store records in an SQLite database.

## Technologies Used

- Python
- Flask
- SQLite
- Requests
- Git
- GitHub

## Project Structure

- `app.py` — Main Flask application and API endpoints.
- `database.py` — Database connection and table creation.
- `test_api.py` — API testing script.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Files excluded from version control.
- `README.md` — Project documentation.

## Installation and Setup

### 1. Clone the Repository

Clone or download the repository from GitHub:

https://github.com/spandan-kar-7/CODSOFT_TASK1

### 2. Install Dependencies

Install the packages listed in `requirements.txt` using Python's package manager.

### 3. Initialize the Database

Run the database initialization script to create the required tables.

### 4. Run the Application

Start the Flask application.

The local server will be available at:

`http://127.0.0.1:5000`

## API Endpoints

### Student Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve student records |
| POST | `/students` | Add a student |
| GET | `/students/<id>` | Retrieve a student by ID |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

### Course Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/courses` | Retrieve all courses |
| POST | `/courses` | Add a course |
| GET | `/courses/<id>` | Retrieve a course by ID |
| PUT | `/courses/<id>` | Update a course |
| DELETE | `/courses/<id>` | Delete a course |

### Enrollment Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/enrollments` | Retrieve all enrollments |
| POST | `/enrollments` | Enroll a student in a course |

## Search, Filtering, and Pagination

The student listing endpoint supports search, course filtering, and pagination through query parameters, depending on the implemented functionality.

## Example API Requests

### Add a Student

**Method:** POST

**Endpoint:** `/students`

Request body:

    {
        "name": "Rahul Das",
        "email": "rahul@example.com",
        "age": 21,
        "course": "CSE AIML"
    }

### Add a Course

**Method:** POST

**Endpoint:** `/courses`

Request body:

    {
        "course_name": "Artificial Intelligence and Machine Learning",
        "description": "BTech CSE AIML Course"
    }

### Enroll a Student

**Method:** POST

**Endpoint:** `/enrollments`

Request body:

    {
        "student_id": 1,
        "course_id": 1
    }

Use valid student and course IDs from your database.

## API Testing

The project includes `test_api.py`, which sends HTTP requests to the running Flask application and displays the responses.

Run the tests after starting the Flask server.

Test results may depend on existing database records. Duplicate records can return conflict responses, while requests involving nonexistent IDs can return not-found responses.

## HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Invalid request data |
| 404 | Resource not found |
| 409 | Duplicate record or other conflict |
| 500 | Internal server error |

## Database Design

The application uses three SQLite tables:

- **Students:** Stores student details.
- **Courses:** Stores course names and descriptions.
- **Enrollments:** Connects students and courses using foreign keys.

Primary keys, foreign keys, and uniqueness constraints help maintain data integrity.

## Learning Outcomes

- RESTful API development using Flask.
- CRUD operations.
- Relational database management using SQLite.
- Input validation and error handling.
- Search, filtering, and pagination.
- API testing using Python Requests.
- Version control using Git and GitHub.

## Internship Information

- **Organization:** CodSoft
- **Role:** Backend Development Intern
- **Internship Type:** Virtual Internship
- **Duration:** 10 October 2026 – 10 November 2026

This project is part of my backend development learning journey during the CodSoft internship.

## Author

**Spandan Kar**

GitHub: [spandan-kar-7](https://github.com/spandan-kar-7)

## License

Developed for educational and internship purposes.
