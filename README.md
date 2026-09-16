<<<<<<< HEAD
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
=======
# DBMS_10 – Project Proposal for the Term Project

**Module:** Introduction to Database Management Systems · THGA Bochum
**Lecturer:** Stephan Bökelmann · <sboekelmann@ep1.rub.de>
**Prerequisites:** Lectures 01–10, exercises DBMS_01–DBMS_09

This exercise is **structured differently** from the previous ones: you do not
write code, you **design** your own database-backed system and submit a
**project proposal** to the lecturer. The proposal is the basis of your **term
project** (graded deliverable), in which you build a complete system over up to
two months (≈ 40 h of real work, including documentation and video).

**Architecture** — everything on the lecture server:

```
Frontend (installed .deb)  --HTTP + X-API-Key-->  FastAPI  -->  PostgreSQL
                                     backend orchestrated by Docker Compose
```

- **Backend** (PostgreSQL + FastAPI) runs in containers via Docker Compose.
- **Frontend** is built as a Debian installer (`.deb`) and installed next to it.
- Write endpoints are protected with an `X-API-Key`.

The term project is submitted as three parts: the **running system**, a
**documentation** (a GitHub repo with LaTeX CI + Makefile), and an **8–10 min
video** (`.mpg` to Moodle *or* an unlisted YouTube link).

## Repository layout

```
src/dbms_10.tex             # the exercise / assignment
proposal-template/          # fill-in skeleton students copy for the proposal
  proposal.tex
example-documentation/      # worked example of the final documentation
  documentation.tex
style/thga-db.sty           # THGA corporate design (copied from the course repo)
.github/workflows/build.yml # LaTeX build + release — copy this into your own repo
Makefile                    # builds all three PDFs into out/
out/                        # generated PDFs (not committed)
```

The `proposal-template/` and `example-documentation/` folders are meant to be
**copied**: start your proposal from the template, and model your documentation
repository on the example — together with the `Makefile` and
`.github/workflows/build.yml`, which build the PDF and publish it as a GitHub
Release on every tag push.

## Build

Requirement: `latexmk` and TeX Live (`apt install latexmk texlive-full`).

```bash
make          # builds out/dbms_10.pdf, out/proposal.pdf, out/documentation.pdf
make clean    # remove auxiliary files, keep PDFs
make distclean# remove everything including out/
```

## Releases

Pushing a tag matching `v*` triggers the GitHub Actions workflow, which builds
all three PDFs and attaches them to a GitHub Release automatically.
>>>>>>> b8e0d93 (Update project)
