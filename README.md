# 🐾 Pet Adoption Management System  

<div align="center">

A full-stack database application for managing pets, adopters, and adoptions  
Built with **FastAPI · PostgreSQL · Docker · Tkinter**

</div>

---

##  Overview

The **Pet Adoption Management System** is a database-driven full-stack application designed to manage the complete pet adoption workflow.

It provides:

- Structured storage using a relational database  
- RESTful API for communication  
- Desktop GUI for user interaction  
- Docker-based environment for reproducibility  

---

##  Objectives

- Implement a **clean 3-tier architecture**
- Apply **database normalization (3NF)**
- Provide **CRUD operations via REST API**
- Separate **UI, business logic, and data layer**
- Enable **easy deployment using Docker**

---

##  System Architecture

| Layer     | Technology        | Responsibility |
|----------|------------------|----------------|
| Frontend | Tkinter (Python) | User interface & interaction |
| Backend  | FastAPI          | Business logic & API endpoints |
| Database | PostgreSQL       | Persistent data storage |

**Architecture Flow:**  
Tkinter GUI → FastAPI → PostgreSQL  

---

## 📁Project Structure

| Folder/File           | Description |
|----------------------|------------|
| `backend/`           | FastAPI application (routes, models, logic) |
| `frontend/`          | Tkinter GUI (`app.py`) |
| `database/`          | SQL schema & seed data |
| `docs/`              | Project documentation (LaTeX) |
| `docker-compose.yml` | Multi-container setup |
| `requirements.txt`   | Python dependencies |
| `README.md`          | Project documentation |

---

##  Technologies Used

| Category          | Technology |
|------------------|-----------|
| Programming      | Python |
| Backend API      | FastAPI |
| ORM              | SQLAlchemy |
| Database         | PostgreSQL |
| Containerization | Docker & Docker Compose |
| GUI              | Tkinter |
| Documentation    | LaTeX |

---

##  Installation & Setup

### 1. Clone Repository

    git clone https://github.com/meryamkaddoum-max/pet-adoption-system.git
    cd pet-adoption-system

---

### 2. Start Backend & Database

    docker compose up --build

### Services after startup:

| Service     | URL / Port |
|------------|-----------|
| API        | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |

---

### 3. Run Frontend (GUI)

    cd frontend
    python app.py

---

##  API Endpoints

###  Pets

| Method | Endpoint       | Description |
|--------|---------------|------------|
| GET    | `/pets`       | Get all pets |
| POST   | `/pets`       | Create a new pet |
| PUT    | `/pets/{id}`  | Update pet |
| DELETE | `/pets/{id}`  | Delete pet |

---

###  Adopters

| Method | Endpoint            | Description |
|--------|--------------------|------------|
| GET    | `/adopters`        | Get all adopters |
| POST   | `/adopters`        | Create adopter |
| DELETE | `/adopters/{id}`   | Delete adopter |

---

###  Adoptions

| Method | Endpoint            | Description |
|--------|--------------------|------------|
| GET    | `/adoptions`       | Get all adoptions |
| POST   | `/adoptions`       | Create adoption |
| DELETE | `/adoptions/{id}`  | Delete adoption |

---

##  Database Design

### Tables Overview

| Table      | Description |
|-----------|------------|
| `pets`     | Stores pet information |
| `adopters` | Stores adopter details |
| `adoptions`| Links pets with adopters |

---

### Table Details

#### 🐾 pets

| Column  | Type         | Description |
|---------|-------------|------------|
| id      | INTEGER (PK) | Unique identifier |
| name    | VARCHAR      | Pet name |
| species | VARCHAR      | Type (dog, cat, etc.) |
| breed   | VARCHAR      | Breed |
| gender  | VARCHAR      | Gender |
| age     | INTEGER      | Age |
| status  | VARCHAR      | Available / Adopted |

---

####  adopters

| Column     | Type         | Description |
|------------|-------------|------------|
| id         | INTEGER (PK) | Unique identifier |
| first_name | VARCHAR      | First name |
| last_name  | VARCHAR      | Last name |
| email      | VARCHAR      | Email |
| phone      | VARCHAR      | Phone number |

---

####  adoptions

| Column        | Type         | Description |
|---------------|-------------|------------|
| id            | INTEGER (PK) | Unique identifier |
| adoption_date | DATE         | Adoption date |
| pet_id        | INTEGER (FK) | References pets |
| adopter_id    | INTEGER (FK) | References adopters |

---

##  Features

- Full CRUD operations  
- REST API with FastAPI  
- Dockerized environment  
- Desktop GUI (Tkinter)  
- PostgreSQL integration  
- Separation of concerns (UI / API / DB)  

---

##  Example Workflow

1. Start Docker containers  
2. Launch GUI  
3. Add pets  
4. Add adopters  
5. Create adoption  
6. View results via GUI or API  

---

##  Documentation

Located in:

    docs/

Compile with:

    pdflatex documentation.tex

---

## ⚠️ Important Notes

- Docker must be running  
- Ports **8000** and **5432** must be free  
- Start backend before frontend  
- API must be accessible at `localhost:8000`  

---

##  Future Improvements

- Authentication (JWT / OAuth)  
- Web frontend (React)  
- Search & filtering  
- Cloud deployment  
- Analytics dashboard  

---

##  Author

**Meriem Kaddoum**  
Information Technology & Digitalization  
THGA Bochum  

---
This project is for educational purposes.
