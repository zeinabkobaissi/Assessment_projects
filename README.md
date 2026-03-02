
# 📚 Library Management System

A full-stack Library Management System designed to manage books, members roles efficiently.  
This project demonstrates backend development, database design, and  AI-powered enhancements.

---

## 🚀 Project Overview

The Library Management System allows administrators to:

- Add, update, and delete and get all books
- Manage library members
- Maintain clean database relationships
  
and allow the the users to :
- Borrow and return books
- Track book availability


This system is built with scalability and clean architecture principles in mind.

---
The project serve with :
Frontend integration(HTML)
role based admin and user
user authentication
REST API documentation (Swagger)
AI integration to ease summary and recommendation of books

## 🏗️ Tech Stack

- **Backend:** Python
- **Framework:** (Flask / FastAPI — adjust if needed)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Environment Management:** dotenv
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
main.py # Application entry point
├── models.py # Database models
├── database.py # Database configuration
├── routes.py # API routes (if applicable)
├── requirements.txt # Project dependencies
├── .env # Environment variables (not committed)
├── .gitignore
|__ services
|__ templates
└── README.md
🗄️ Database Design

The system uses relational database principles with the following core entities:

### 📖 Book
- id
- title
- author
- description
- publication_year
- genre
- availability_status
  
  Core Features

### ✅ Book Management
- Add new books
- Update book information
- Delete books
- get all books

###🤖  AI Enhancements (If Implemented)

- Smart book recommendations

- Automated summaries

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/zeinabkobaissi/Library_management.git
cd Library_management
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create a .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/library_db

⚠️ Do NOT commit this file.

▶️ Running the Application
python main.py

Or if using FastAPI:

uvicorn main:app --reload
🛡️ Security Practices

Environment variables are stored in .env

.env is excluded from version control

API keys are never hardcoded

Database credentials are protected

📈 Future Improvements

User authentication (JWT)

Deployment on cloud (Render / Railway / AWS)

Docker containerization


🎯 Learning Outcomes

This project demonstrates:

Database schema design

ORM usage with SQLAlchemy

Backend architecture structuring

Secure environment configuration

Clean code organization
