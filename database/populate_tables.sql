-- Initialize blood bank tables

INSERT INTO blood_bank (BloodBankID, ManagerID, StreetAddress) VALUES
        (1, 1, '101 1st Street'),
        (2, 2, '202 2nd Street'),
        (3, 3, '303 3rd Street');

INSERT INTO blood_bank_employee (BloodBankID, FullName, DateOfBirth, SSN, PasswordSalt, PasswordHash, StreetAddress, PhoneNumber) VALUES
        (1, 'Michael Chung', '1988-5-19', 456179224, 'salt0', 'hash0', '24 West 22 St.', '656-177-479'),
        (0, 'Christopher Chen', '1990-5-17', 389508378, 'salt1', 'hash1', '65 East 26 St.', '211-350-305'),
        (1, 'Jessica Melton', '1966-4-20', 444825683, 'salt2', 'hash2', '1 South 35 St.', '523-386-918'),
        (3, 'Matthew Hill', '1978-12-23', 392854820, 'salt3', 'hash3', '85 East 18 St.', '802-330-287'),
        (1, 'Ashley Puckett', '1952-6-28', 199286255, 'salt4', 'hash4', '41 East 33 St.', '226-680-248');

INSERT INTO blood_bank_manager (BloodBankID, ManagerID) VALUES
        (1, 1),
        (2, 2),
        (3, 3);

-- Initialize hospital tables

INSERT INTO hospital (HospitalID, StreetAddress) VALUES
        (1, '101 1st Street'),
        (2, '202 2nd Street');

INSERT INTO hospital_employee (HospitalID, FullName, DateOfBirth, SSN, PasswordSalt, PasswordHash, StreetAddress, PhoneNumber) VALUES
        (1, 'Michael Chung', '1988-5-19', 456179224, 'salt0', 'hash0', '24 West 22 St.', '656-177-479'),
        (2, 'Christopher Chen', '1990-5-17', 389508378, 'salt1', 'hash1', '65 East 26 St.', '211-350-305'),
        (1, 'Jessica Melton', '1966-4-20', 444825683, 'salt2', 'hash2', '1 South 35 St.', '523-386-918'),
        (2, 'Matthew Hill', '1978-12-23', 392854820, 'salt3', 'hash3', '85 East 18 St.', '802-330-287'),
        (1, 'Ashley Puckett', '1952-6-28', 199286255, 'salt4', 'hash4', '41 East 33 St.', '226-680-248');