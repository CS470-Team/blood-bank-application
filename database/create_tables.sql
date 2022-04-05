USE bloodbank;

-- Drop all tables
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS blood_donation;
DROP TABLE IF EXISTS blood_transfusion;
DROP TABLE IF EXISTS blood_bank;
DROP TABLE IF EXISTS blood_bank_employee;
DROP TABLE IF EXISTS hospital;
DROP TABLE IF EXISTS hospital_employee;

CREATE TABLE IF NOT EXISTS client (
    ClientID INTEGER PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(50) NOT NULL,
    BloodType TEXT NOT NULL,
    EmailAddress TEXT NOT NULL,
    StreetAddress TEXT NOT NULL,
    DateOfBirth TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    PasswordHash TEXT NOT NULL,
    PasswordSalt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS blood_bank (
    BloodBankID INTEGER PRIMARY KEY AUTO_INCREMENT,
    ManagerID INTEGER UNIQUE NOT NULL,
    StreetAddress VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS blood_bank_employee (
    EmployeeID INTEGER PRIMARY KEY AUTO_INCREMENT,
    BloodBankID INTEGER NOT NULL,
    FullName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    SSN INTEGER NOT NULL,
    PasswordSalt TEXT NOT NULL,
    PasswordHash TEXT NOT NULL,
    StreetAddress VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    FOREIGN KEY(BloodBankID) REFERENCES blood_bank(BloodBankID)
);

-- add foreign key constraint to blood_bank
ALTER TABLE blood_bank
ADD CONSTRAINT FK_BloodBank_Manager FOREIGN KEY(ManagerID) REFERENCES blood_bank_employee(EmployeeID);

CREATE TABLE IF NOT EXISTS hospital (
    HospitalID INTEGER PRIMARY KEY AUTO_INCREMENT,
    HospitalName VARCHAR(80) NOT NULL,
    StreetAddress TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS hospital_employee (
    EmployeeID INTEGER PRIMARY KEY AUTO_INCREMENT,
    HospitalID INTEGER NOT NULL,
    FullName VARCHAR(50) NOT NULL,
    FOREIGN KEY(HospitalID) REFERENCES hospital(HospitalID)
);

CREATE TABLE IF NOT EXISTS blood_transfusion (
    TransfusionID INTEGER PRIMARY KEY AUTO_INCREMENT,
    EmployeeID INTEGER NOT NULL,
    TransfusionDate DATE NOT NULL,
    Amount INTEGER NOT NULL,
    RecipientID INTEGER NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES hospital_employee(EmployeeID),
    FOREIGN KEY (RecipientID) REFERENCES client(ClientID)
);

CREATE TABLE IF NOT EXISTS blood_donation (
    DonationID INTEGER PRIMARY KEY AUTO_INCREMENT,
    EmployeeID INTEGER NOT NULL,
    DonorID INTEGER NOT NULL,
    ScreenResult TEXT NOT NULL,
    DonationDate DATE NOT NULL,
    Amount INTEGER NOT NULL,
    FOREIGN KEY(EmployeeID) REFERENCES blood_bank_employee(EmployeeID),
    FOREIGN KEY(DonorID) REFERENCES client(ClientID)
);