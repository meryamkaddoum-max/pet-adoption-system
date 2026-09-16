-- Insert shelters
INSERT INTO Shelter (name, address, phone)
VALUES
('Happy Paws Shelter', '123 Main Street, Bochum', '+49 234 111111'),
('Safe Haven Shelter', '45 Park Road, Essen', '+49 201 222222');

-- Insert pets
INSERT INTO Pet (name, species, breed, age, gender, status, shelter_id)
VALUES
('Max', 'Dog', 'Labrador', 3, 'Male', 'Available', 1),
('Luna', 'Cat', 'Persian', 2, 'Female', 'Available', 1),
('Bella', 'Dog', 'Beagle', 5, 'Female', 'Adopted', 2);

-- Insert adopters
INSERT INTO Adopter (first_name, last_name, email, phone)
VALUES
('John', 'Smith', 'john.smith@example.com', '+49 151 12345678'),
('Emma', 'Miller', 'emma.miller@example.com', '+49 151 87654321');

-- Insert adoptions
INSERT INTO Adoption (adoption_date, status, pet_id, adopter_id)
VALUES
('2026-08-01', 'Completed', 3, 1);