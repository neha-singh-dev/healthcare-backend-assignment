# Healthcare Backend Assignment

A Django REST Framework backend for a healthcare system built as part of my internship assignment.

---

## Tech Stack
- Python 3.8+
- Django
- Django REST Framework
- JWT Authentication (Simple JWT)
- SQLite3

---

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/neha-singh-dev/healthcare-backend-assignment.git
cd healthcare-backend-assignment
```
### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py migrate
```
### 5. Run the server
```bash
python manage.py runserver
```
Server will start at:
http://127.0.0.1:8000/

---

### Authentication (JWT)

This project uses JSON Web Tokens (JWT) for securing API endpoints.

### Get Token Pair (Login)

-POST `/api/auth/login/`

Example request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Example response:
```json
{
  "refresh": "<JWT_REFRESH_TOKEN>",
  "access": "<JWT_ACCESS_TOKEN>"
}
```



### Use JWT Access Token

For all protected endpoints, include this header:
```
Authorization: Bearer <JWT_ACCESS_TOKEN>
```
---

### API Endpoints

### Patient

-GET `/api/patients/`

-POST `/api/patients/`

-GET `/api/patients/<id>/`

-PUT `/api/patients/<id>/`

-DELETE `/api/patients/<id>/`

### Doctor

-GET `/api/doctors/`

-POST `/api/doctors/`

-GET `/api/doctors/<id>/`

-PUT `/api/doctors/<id>/`

-DELETE `/api/doctors/<id>/`

### Mapping (Patient-Doctor)

-GET `/api/mappings/`

-POST `/api/mappings/`

-GET `/api/mappings/<id>/`

-PUT `/api/mappings/<id>/`

-DELETE `/api/mappings/<id>/`

### Features

-Full CRUD for Patient, Doctor, and Mapping models

-Foreign key relationship between Patient and Doctor

-JWT-based authentication

-Clean REST API structure

---





