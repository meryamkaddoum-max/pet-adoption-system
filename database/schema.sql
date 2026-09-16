CREATE TABLE Shelter (
    shelter_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20)
);
CREATE TABLE Pet (
    pet_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50) NOT NULL,
    breed VARCHAR(100),
    age INTEGER,
    gender VARCHAR(10),
    status VARCHAR(20) NOT NULL,
    shelter_id INTEGER NOT NULL,
    FOREIGN KEY (shelter_id) REFERENCES Shelter(shelter_id)
);
CREATE TABLE Adopter (
    adopter_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(20)
);
CREATE TABLE Adoption (
    adoption_id SERIAL PRIMARY KEY,
    adoption_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    pet_id INTEGER NOT NULL,
    adopter_id INTEGER NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES Pet(pet_id),
    FOREIGN KEY (adopter_id) REFERENCES Adopter(adopter_id)
);