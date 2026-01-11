# Internship-application-tracker

This project is a backend-focused web application which is designed for users to help track their internships and job applications in a structured and maintainable way.

The aim of this project is to demonstrate core backend engineering skills, along with clean architecture, data modeling, validation and API design.

## Tech Stack

      - Python
      - Flask
      - SQLite
      - SQLAlchemy

## Features

      - Create, update, and delete internship and job applications
      - Track application status (Applied, interview, Rejected, Offer)
      - Store application notes and dates
      - RESTful API endpoints to manage application

## Project Focus

This project will focus on backend design, maintainability, and clarity rather than UI complexity.

## Why this project

Tracking applications manually results in an error-prone and unstructured application. This application aims to provide a clean backend system that can be extended with additional features for e.g, authentication, analytics, or a frontend interface.

## Status

    1. Project setup and design phase

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

      
