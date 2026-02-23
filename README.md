# Healthcare Backend Assignment

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Django](https://img.shields.io/badge/Django-6.0.2-green)
![License](https://img.shields.io/badge/License-MIT-blue)

A Django REST Framework backend for a healthcare system built as part of my internship assignment.

---

## Tech Stack
- Python 3.8+
- Django
- Django REST Framework
- JWT Authentication (Simple JWT)
- PostgreSQL

---

## Project Structure
```
healthcare_backend/
│
├── patients/        # Patient model and APIs  
├── doctors/         # Doctor model and APIs  
├── mappings/        # Patient-Doctor mapping  
├── healthcare/      # Main project settings   
└── manage.py  
```
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
### 4. Configure PostgreSQL

- Make sure PostgreSQL is installed
- Create a database, e.g. healthcare_db
```bassh
createdb healthcare_db
```
- Update settings.py DATABASES section:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 5. Apply migrations
```bash
python manage.py migrate
```
###  5.Create Superuser(optional, for testing JWT-protected endpoints)
```bash
python manage.py createsuperuser
```
### 6. Run the server
```bash
python manage.py runserver
```
Server will start at:
```
http://127.0.0.1:8000/
```
---

### Authentication (JWT)

This project uses JSON Web Tokens (JWT) for securing API endpoints.

### Get Token Pair (Login)

POST `/api/auth/login/`

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

### API Endpoints & Example Payloads

### Patient

- GET `/api/patients/`
- POST `/api/patients/`

Example POST request:
```json
{
  "name": "John Doe",
  "age": 35,
  "medical_history": "Lung Cancer"
}
```
Response:
```json
{
  "id": 1,
  "name": "John Doe",
  "age": 35,
"medical_history": "Lung Cancer"
}
```
- GET/PUT/DELETE `/api/patients/<id>/`

---

### Doctor

- GET `/api/doctors/`
- POST `/api/doctors/`

Example POST request:
```json
{
  "name": "Dr. Smith",
  "specialization": "Cardiology",
  "email": "drsmith@example.com",
  "experience_years": 7
}
```
Response:
```json
{
  "id": 1,
  "name": "Dr. Smith",
  "specialization": "Cardiology",
  "email": "drsmith@example.com",
  "experience_years": 7
}
```
- GET/PUT/DELETE `/api/doctors/<id>/`

---

### Patient-Doctor Mapping

- GET `/api/mappings/`
- POST `/api/mappings/`

Example POST request:
```json
{
  "patient": 1,
  "doctor": 1,
}
```
Response:
```json
{
  "id": 1,
  "patient": 1,
  "doctor": 1,
}
```
- GET/PUT/DELETE `/api/mappings/<id>/`

---

### Features

- Full CRUD for Patient, Doctor, and Mapping models

- Foreign key relationship between Patient and Doctor

- JWT-based authentication

- Clean REST API structure

## Future Improvements
- Add role-based access control (Admin, Doctor)
- Add pagination for large datasets
- Add unit tests
- Deploy to cloud (Render / Railway / AWS)

---





