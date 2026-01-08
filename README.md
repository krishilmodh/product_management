# Product Management System

A Django-based web application built as part of an interview assessment.  
The system supports user authentication, role-based access control, product management, and REST APIs secured with JWT.

---

## Features

- User registration and login
- Role-based access (Admin & User)
- Admin can add, edit, and delete products
- Users have read-only access to products
- Product list displayed on homepage
- Product detail page
- Secure authentication using:
  - Django sessions (web UI)
  - JWT (REST APIs)
- Modern dark-themed UI using Tailwind CSS and DaisyUI

---

## Tech Stack

- Backend: Django, Django REST Framework
- Frontend: HTML, Tailwind CSS, DaisyUI
- Authentication: Django Sessions, JWT (SimpleJWT)
- Database: SQLite

---

## Setup & Run

```bash
pip install django djangorestframework djangorestframework-simplejwt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

If python does not work, use python3.
```

## Open in browser:
http://127.0.0.1:8000/


## API (JWT)

- POST /api/auth/register/
- POST /api/auth/login/
- GET /api/products/
- POST /api/products/create/ (Admin only)
