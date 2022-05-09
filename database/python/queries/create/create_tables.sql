USE bloodbank;

CREATE TABLE IF NOT EXISTS client (
    ClientId INTEGER PRIMARY KEY AUTO_INCREMENT,
    FullName TEXT NOT NULL,
    BloodType TEXT NOT NULL,
    EmailAddress VARCHAR(255) UNIQUE NOT NULL,
    HomeAddress TEXT NOT NULL,
    DateOfBirth TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    PasswordSalt TEXT NOT NULL,
    PasswordHash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS blood_bank (
    BloodBankId INTEGER PRIMARY KEY AUTO_INCREMENT,
    ManagerId INTEGER UNIQUE NOT NULL,
    StreetAddress VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS blood_bank_employee (
    EmployeeId INTEGER AUTO_INCREMENT,
    EmployerId INTEGER NOT NULL,
    FullName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Ssn INTEGER NOT NULL,
    PasswordSalt TEXT NOT NULL,
    PasswordHash TEXT NOT NULL,
    HomeAddress VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    PRIMARY KEY (EmployeeId)
);

CREATE TABLE IF NOT EXISTS hospital (
    HospitalId INTEGER PRIMARY KEY AUTO_INCREMENT,
    HospitalName VARCHAR(80) NOT NULL,
    StreetAddress TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS hospital_employee (
    EmployeeId INTEGER PRIMARY KEY AUTO_INCREMENT,
    EmployerId INTEGER NOT NULL,
    FullName VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS blood_transfusion (
    TransfusionId INTEGER PRIMARY KEY AUTO_INCREMENT,
    EmployeeId INTEGER NOT NULL,
    TransfusionDate DATE NOT NULL,
    Amount INTEGER NOT NULL,
    RecipientId INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS blood_donation (
    DonationId INTEGER PRIMARY KEY AUTO_INCREMENT,
    EmployeeId INTEGER NOT NULL,
    DonorId INTEGER NOT NULL,
    ScreenResult TEXT NOT NULL,
    DonationDate DATE NOT NULL,
    Amount INTEGER NOT NULL
);