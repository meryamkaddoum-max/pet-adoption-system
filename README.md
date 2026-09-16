# 🐾 Pet Adoption Management System

<div align="center">

A full-stack application for managing pets, adopters, and adoptions  
Built with ❤️ using FastAPI, PostgreSQL, Docker & Tkinter  

</div>

---

## 🚀 Overview

The **Pet Adoption Management System** is a database-driven application designed to manage the entire adoption process.

It allows users to:

- Register and manage pets  
- Manage adopter information  
- Record and track adoptions  
- Interact via a REST API  
- Use a desktop GUI (Tkinter)  

---

## 🏗️ Architecture

The system follows a 3-layer architecture:

Frontend (Tkinter GUI)  
↓  
Backend (FastAPI REST API)  
↓  
Database (PostgreSQL)  

- Clear separation of concerns  
- Scalable and maintainable design  
- API-based communication  

---

## 📁 Project Structure

Pet-Adoption-Management-System/  
│  
├── backend/              # FastAPI backend  
├── frontend/             # Tkinter GUI (app.py)  
├── database/             # schema.sql & seed.sql  
├── docs/                 # LaTeX documentation  
├── docker-compose.yml  
├── requirements.txt  
└── README.md  

---

## ⚙️ Technologies Used

- Python  
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- Docker & Docker Compose  
- Tkinter  
- LaTeX  

---

## 🐳 Installation & Setup

### 1. Clone the repository

git clone https://github.com/meryamkaddoum-max/pet-adoption-system.git  
cd pet-adoption-system  

---

### 2. Start backend & database

docker compose up --build  

After startup:

- API → http://localhost:8000  
- Swagger UI → http://localhost:8000/docs  
- Database → localhost:5432  

---

### 3. Run frontend (GUI)

Open a new terminal:

cd frontend  
python app.py  

---

## 📡 API Endpoints

### Pets
GET /pets  
POST /pets  
PUT /pets/{id}  
DELETE /pets/{id}  

### Adopters
GET /adopters  
POST /adopters  
DELETE /adopters/{id}  

### Adoptions
GET /adoptions  
POST /adoptions  
DELETE /adoptions/{id}  

---

## 🗄️ Database Design

Tables:

pets  
- id, name, species, breed, gender, age, status  

adopters  
- id, first_name, last_name, email, phone  

adoptions  
- id, adoption_date, pet_id, adopter_id  

- Normalized (3NF)  
- Uses foreign keys  
- No redundant data  

---

## 🖥️ Features

- Full CRUD operations  
- REST API with FastAPI  
- Dockerized environment  
- GUI for interaction  
- PostgreSQL integration  

---

## 📄 Documentation

Located in:

docs/  

Compile with:

pdflatex documentation.tex  

---

## ⚠️ Important Notes

- Docker must be running  
- Ports 8000 and 5432 must be free  
- Start backend before frontend  
- API must run at localhost:8000  

---

## 🧪 Example Workflow

1. Start Docker  
2. Open GUI  
3. Add pets  
4. Add adopters  
5. Create adoption  
6. View results  

---

## 🔮 Future Improvements

- Authentication (JWT)  
- Web frontend (React)  
- Search & filtering  
- Cloud deployment  

---

## 👩‍💻 Author

Meriem Kaddoum  
Information Technology & Digitalization  
THGA Bochum  

---


This project is for educational purposes.
