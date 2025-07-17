# 👩‍💻 Full Stack Employee Management System

This is a full-stack web application built with **React.js (Frontend)** and **Django REST Framework (Backend)**. It allows users to **Create**, **Read**, **Update**, and **Delete (CRUD)** employee records, complete with validation and a user-friendly interface.

---

## 📌 Features

- 🧾 View all employees
- ➕ Add new employees
- ✏️ Edit existing employee details
- ❌ Delete employees
- 🔐 Password field support
- ✅ Form validation (frontend & backend)
- 📡 API integration using Axios
- 🌐 CORS enabled for smooth communication

---

## 🛠 Tech Stack

### 🚀 Frontend:
- React.js
- React Hook Form
- React Router DOM
- Axios
- CSS

### ⚙️ Backend:
- Django
- Django REST Framework
- PostgreSQL
- CORS Headers

---

## 🧾 Folder Structure

employee-management/
├── backend/ # Django project (mysite)
│ ├── api/ # Django app
│ └── manage.py # Django entry point
│
├── frontend/ # React app
│ ├── src/
│ │ ├── components/
│ │ │ ├── EmployeeDetails.js
│ │ │ └── EmployeeFormPage.js
│ │ └── App.js
│ ├── App.css
│ └── index.js
│
├── README.md
└── requirements.txt

yaml
Copy
Edit

---

## 🔌 How to Run the Project

### 1️⃣ Backend (Django)

```bash
cd backend
python -m venv env
env\Scripts\activate      # On Windows
pip install -r requirements.txt
python manage.py runserver
Ensure PostgreSQL is installed and configured properly. Add your DB details in settings.py.

2️⃣ Frontend (React)
bash
Copy
Edit
cd frontend
npm install
npm start
The app will run on: http://localhost:3000
API will be served from: http://127.0.0.1:8000/api/

🧪 API Endpoints
Method	Endpoint	Description
GET	/api/employees/	List all employees
POST	/api/employees/create/	Create new employee
GET	/api/employees/<id>/	Retrieve specific employee
PUT	/api/employees/<id>/update/	Update employee details
DELETE	/api/employees/<id>/delete/	Delete employee

📋 Form Fields
username (required)

first_name (required)

last_name (required)

email (required, email format)

password (required)

Validation is implemented on both frontend (React Hook Form) and backend (Django serializers).

🧑‍🎓 Author
Alisha Shehzad
Final Year BSc Computer Science
University of Hertfordshire
