# Student Management System

## Project Description

This project is a Student Management System developed as part of my academic work, following a structured and methodical development approach. The system was initially designed using software engineering principles, where detailed system models and diagrams were created to define the architecture, workflow, and logical structure of the application. This design phase ensured a clear and scalable foundation before implementation.

Following the design stage, the system was developed using Python and Django, focusing on building a robust backend capable of efficiently managing student records, user authentication, and overall system operations. PostgreSQL was integrated as the database to handle structured data storage and retrieval in a reliable and scalable manner.

The application is containerized using Docker, allowing for a consistent and portable development environment. Docker ensures that all dependencies and services are properly configured, making the system easier to deploy and run across different environments.

The project demonstrates my ability to translate theoretical concepts into a functional real-world application. It highlights my understanding of system design, backend development, database management, and containerization, as well as my capability to follow a complete development lifecycle from planning and design to implementation and testing.

---

## Features

* Student data management (add, update, delete, view)
* User authentication and access control
* Structured backend system using Django
* Integration with PostgreSQL database (pgAdmin)
* Containerized environment using Docker
* Organized and modular project architecture

---

## Technologies Used

* Python
* Django
* PostgreSQL (pgAdmin)
* Docker
* HTML
* CSS
* Bootstrap

---

## Project Structure

* Core application modules (students, users, etc.)
* Templates for frontend rendering
* Static files (CSS, JS, media)
* Backend logic and configuration
* Docker configuration files
* docs/ – contains academic project reports

---

## Documentation

* Software Engineering Report
* Python Project Report
* Software Testing Report

---

## Installation and Setup

### Prerequisites

* Python installed
* PostgreSQL installed and configured
* Docker installed

---

## Instructions

* Clone the repository
  git clone [https://github.com/ranaarman8903/student-management-system.git](https://github.com/ranaarman8903/student-management-system.git)

* Navigate to the project folder
  cd student-management-system

* Build and run Docker containers
  docker compose up --build

* Open a new terminal and check running containers
  docker ps

* Access the container
  docker exec -it <container_id> bash

* Run migrations
  python manage.py makemigrations
  python manage.py migrate

* Create superuser
  python manage.py createsuperuser

* Open in browser
  [http://localhost:8000/](http://localhost:8000/)

* Admin panel
  [http://localhost:8000/admin](http://localhost:8000/admin)

---

## Usage

* Run the application using Docker
* Access the system through the browser
* Log in using the created superuser account
* Manage student records through the admin panel
* Navigate across modules to perform system operations

---

## Author

Arman Rana Muhammad
