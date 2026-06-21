# Secure Login System

## Overview

Secure Login System is a web application built using Python Flask and SQLite that provides secure user authentication. The system uses bcrypt password hashing, input validation, SQL injection protection, session management, and logout functionality to enhance security.

## Features

* User Registration
* User Login Authentication
* Password Hashing using bcrypt
* SQL Injection Protection with Parameterized Queries
* Input Validation
* Session Management
* Secure Logout Functionality
* SQLite Database Integration

## Technologies Used

* Python
* Flask
* SQLite
* bcrypt
* HTML

## Project Structure

SecureLoginSystem/

├── app.py

├── users.db

└── templates/

    ├── register.html

    ├── login.html

    └── dashboard.html

## Installation

1. Clone the repository:
   git clone <repository-url>

2. Navigate to the project folder:
   cd SecureLoginSystem

3. Install required packages:
   pip install flask bcrypt

4. Run the application:
   python app.py

5. Open the browser and visit:
   http://127.0.0.1:5000

## Security Features

### Password Hashing

Passwords are hashed using bcrypt before being stored in the database.

### SQL Injection Prevention

Parameterized SQL queries are used to prevent SQL injection attacks.

### Session Management

User sessions are maintained after successful login and cleared during logout.

### Input Validation

Username and password inputs are validated before processing.

## Future Enhancements

* Two-Factor Authentication (2FA)
* Email Verification
* Password Reset Feature
* Account Lockout After Multiple Failed Attempts
* Password Strength Meter

## Learning Outcomes

* Implement secure authentication systems
* Understand password hashing techniques
* Prevent SQL injection vulnerabilities
* Manage user sessions securely
* Build secure web applications using Flask

## Author

Pavithra A.B.
B.Tech Computer Science Engineering
