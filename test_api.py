import requests

BASE_URL = "http://127.0.0.1:5000"

# 1. Add a student
student_data = {
    "name": "Rahul Das",
    "email": "rahul@example.com",
    "age": 21,
    "course": "CSE AIML"
}

response = requests.post(
    f"{BASE_URL}/students",
    json=student_data
)

print("ADD STUDENT:", response.status_code)
print(response.json())


# 2. View all students
response = requests.get(f"{BASE_URL}/students")

print("\nVIEW STUDENTS:", response.status_code)
print(response.json())

# 3. Update student
student_id = 2

updated_data = {
    "name": "Rahul Das",
    "email": "rahul@example.com",
    "age": 22,
    "course": "Computer Science"
}

response = requests.put(
    f"{BASE_URL}/students/{student_id}",
    json=updated_data
)

print("\nUPDATE STUDENT:", response.status_code)
print(response.json())


# 4. View updated student
response = requests.get(
    f"{BASE_URL}/students/{student_id}"
)

print("\nVIEW UPDATED STUDENT:", response.status_code)
print(response.json())


# 5. Delete student
response = requests.delete(
    f"{BASE_URL}/students/{student_id}"
)

print("\nDELETE STUDENT:", response.status_code)
print(response.json())

# 6. Add students for testing search and pagination

test_students = [
    {
        "name": "Amit Sharma",
        "email": "amit@example.com",
        "age": 20,
        "course": "CSE AIML"
    },
    {
        "name": "Priya Das",
        "email": "priya@example.com",
        "age": 21,
        "course": "CSE"
    },
    {
        "name": "Rahul Sen",
        "email": "rahul.sen@example.com",
        "age": 22,
        "course": "CSE AIML"
    }
]

for student in test_students:
    response = requests.post(
        f"{BASE_URL}/students",
        json=student
    )
    print("ADD TEST STUDENT:", response.status_code)


# 7. Search students by name or email

response = requests.get(
    f"{BASE_URL}/students",
    params={"search": "Amit"}
)

print("\nSEARCH RESULT:", response.status_code)
print(response.json())


# 8. Filter students by course

response = requests.get(
    f"{BASE_URL}/students",
    params={"course": "CSE AIML"}
)

print("\nFILTER RESULT:", response.status_code)
print(response.json())


# 9. Test pagination

response = requests.get(
    f"{BASE_URL}/students",
    params={"page": 1, "limit": 2}
)

print("\nPAGINATION RESULT:", response.status_code)
print(response.json())

# 10. Add a course

course_data = {
    "course_name": "Artificial Intelligence and Machine Learning",
    "description": "BTech CSE AIML Course"
}

response = requests.post(
    f"{BASE_URL}/courses",
    json=course_data
)

print("\nADD COURSE:", response.status_code)
print(response.json())


# 11. View all courses

response = requests.get(f"{BASE_URL}/courses")

print("\nVIEW COURSES:", response.status_code)
print(response.json())

# 12. Enroll a student in a course

enrollment_data = {
    "student_id": 6,
    "course_id": 1
}

response = requests.post(
    f"{BASE_URL}/enrollments",
    json=enrollment_data
)

print("\nADD ENROLLMENT:", response.status_code)
print(response.json())


# 13. View all enrollments

response = requests.get(
    f"{BASE_URL}/enrollments"
)

print("\nVIEW ENROLLMENTS:", response.status_code)
print(response.json())