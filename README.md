# Student Record Management API

A RESTful API developed using Python, Flask, and SQLite to manage student records, courses, and course enrollments. This project demonstrates backend development concepts, database management, API design, input validation, and error handling.

## Project Overview

The Student Record Management API provides endpoints to create, retrieve, update, and delete student and course records. It also supports student enrollment in courses.

The project is designed to demonstrate practical backend development skills using Flask and SQLite.

## Features

### Student Management
- Add new student records.
- Retrieve all student records.
- Retrieve individual student details by ID.
- Update existing student information.
- Delete student records.
- Prevent duplicate email addresses.

### Course Management
- Add new courses.
- Retrieve all available courses.
- Retrieve individual course details.
- Update existing course information.
- Delete courses.
- Prevent duplicate course names.

### Enrollment Management
- Enroll students in courses.
- Retrieve all enrollment records.
- Validate student and course IDs.
- Prevent duplicate enrollments.
- Maintain relationships between students, courses, and enrollments.

### Additional Features
- Search students by name or email.
- Filter student records by course.
- Paginate student records.
- Validate incoming JSON data.
- Handle errors using appropriate HTTP status codes.
- Store records in an SQLite database.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | REST API development |
| SQLite | Database management |
| Requests | API testing |
| Git | Version control |
| GitHub | Source code hosting |

## Project Structure

CODSOFT_TASK1/
│
├── app.py
├── database.py
├── test_api.py
├── requirements.txt
├── .gitignore
├── README.md
└── students.db


**Note:** The SQLite database file is generated locally and is excluded from the GitHub repository.

## Installation and Setup

### 1. Clone the Repository

git clone https://github.com/spandan-kar-7/CODSOFT_TASK1.git

Navigate to the project directory:

cd CODSOFT_TASK1

### 2. Install Dependencies

Install the required Python packages:

python -m pip install -r requirements.txt

### 3. Initialize the Database

Run the following command to create the required database tables:

python database.py

This initializes the Students, Courses, and Enrollments tables.

### 4. Start the Flask Application

Run:

python app.py

The application will be available locally at:

http://127.0.0.1:5000

## API Endpoints

### Student Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve student records |
| POST | `/students` | Add a new student |
| GET | `/students/<id>` | Retrieve a student by ID |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

### Course Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/courses` | Retrieve all courses |
| POST | `/courses` | Add a new course |
| GET | `/courses/<id>` | Retrieve a course by ID |
| PUT | `/courses/<id>` | Update a course |
| DELETE | `/courses/<id>` | Delete a course |

### Enrollment Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/enrollments` | Retrieve all enrollments |
| POST | `/enrollments` | Enroll a student in a course |

## Student Search, Filtering, and Pagination

The student listing endpoint supports additional query parameters, depending on the implemented functionality.

Examples:

### Search Students

GET /students?search=Amit

Search for students using a name or email query.

### Filter Students by Course

GET /students?course=CSE%20AIML

Retrieve students associated with the specified course.

### Paginate Student Records

GET /students?page=1&limit=10

Retrieve a specific page of student records.

## Example API Requests

### Add a Student

**Endpoint:**

POST /students

**JSON Request Body:**

{
    "name": "Rahul Das",
    "email": "rahul@example.com",
    "age": 21,
    "course": "CSE AIML"
}


### Add a Course

**Endpoint:**

POST /courses

**JSON Request Body:**

{
    "course_name": "Artificial Intelligence and Machine Learning",
    "description": "BTech CSE AIML Course"
}

### Enroll a Student

**Endpoint:**


POST /enrollments


**JSON Request Body:**

{
    "student_id": 1,
    "course_id": 1
}

Replace the student and course IDs with valid IDs from your database.

## API Testing

The project includes a Python test script named `test_api.py`.

Run the script using:

python test_api.py

The test script sends HTTP requests to the running Flask application and displays the responses.

**Important:** Start the Flask server before running the test script. Some tests may return conflict or not-found responses if the database already contains the relevant records or if the script uses an outdated ID.

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created successfully |
| 400 | Invalid request data |
| 404 | Resource not found |
| 409 | Conflict, such as a duplicate record |
| 500 | Internal server error |

## Database Design

The application uses three SQLite tables:

- **Students:** Stores student details such as name, email, age, and course.
- **Courses:** Stores course names and descriptions.
- **Enrollments:** Connects students with courses using foreign keys.

The database uses primary keys, foreign keys, and uniqueness constraints to maintain data integrity.

## Learning Outcomes

Through this project, I worked on:

- Developing RESTful APIs using Flask.
- Implementing CRUD operations.
- Managing relational data using SQLite.
- Validating API requests.
- Handling errors and HTTP status codes.
- Implementing search, filtering, and pagination.
- Testing API endpoints using Python Requests.
- Managing source code using Git and GitHub.

## Internship Information

**Organization:** CodSoft  
**Internship Role:** Backend Development Intern  
**Internship Type:** Virtual Internship  
**Duration:** 10 October 2026 – 10 November 2026

This project is part of my backend development learning journey during the CodSoft internship.

## Author

**Spandan Kar**

GitHub: https://github.com/spandan-kar-7

## License

This project was developed for educational and internship purposes.
