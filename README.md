# Internship-application-tracker

This project is a backend-focused web application which is designed for users to help track their internships and job applications in a structured and maintainable way.
This project was built as a learning-focused backend system, demonstrating REST API design, validation, and basic data management.
The aim of this project is to demonstrate core backend engineering skills, along with clean architecture and data modeling.

## Tech Stack

      - Python
      - Flask
      - SQLite
      - SQLAlchemy

## Features

      - Create a new Internship Application 
      - Retreive all Applications
      - Retreive a specific application by index
      - Delete an application
      - Input validation and error handling
      - RESTful API endpoints to manage application

## Project Focus

This project will focus on backend design, maintainability, and clarity rather than UI complexity.

## Why this project

Tracking applications manually results in an error-prone and unstructured application. This application aims to provide a clean backend system that can be extended with additional features for e.g, authentication, analytics, or a frontend interface.

## Data Model

### Application
     - id (int, primary key)
     - company_name(string, required)
     - role_title(string, required)
     - status (string: Applied, Interview, Rejected, Offer)
     - date_applied (date, optional)
     - notes (text, optional)
     
### Application Creation Flow
    1. User Submits Application Details.
    2. Backend validates required fields.
    3. Status is checked against allowed values.
    4. Application is saved to the database.
    5. Backend returns a successful response.

## Validation Rules
    - company_name must not be empty.
    - role_title must not be empty.
    - status must be one of: Applied, Interview, Rejected, Offer

## Current Features

This  project is a simple Flask-based backend for tracking internship applications

### Supported API Endpoints

#### 'GET /applications'

  -  Returns all Internship Applictaions

#### 'POST /applications'
  -  Adds a new Internship application
  -  Requires 'company_name', 'role_title', and 'status'

#### 'GET /applications/<index>'
  - Returns a single application by index
  - Returns 404 if the application does not exist

#### 'DELETE /applications/<index>'
  - Deletes an application by index
  - Returns 404 if the application does not exist

## How to Run Locally 

1. Clone the repository
   
       git clone https://github.com/msaim366/Internship-application-tracker.git
       cd Internship-application-tracker
2. Create and Activate a virtual Environment

       python -m venv .venv
       .venv\Scripts\activate
3. Install dependencies
   
       pip install -r requirements.txt
        
4. Run the application

       python app/run.py 

6. The app will run at

       http://127.0.0.1:5001

   





      
