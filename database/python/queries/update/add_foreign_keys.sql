START TRANSACTION;
SET FOREIGN_KEY_CHECKS=0; 
ALTER TABLE blood_bank_employee
ADD FOREIGN KEY (BloodBankId) REFERENCES blood_bank(BloodBankId);

ALTER TABLE hospital_employee
ADD FOREIGN KEY (HospitalId) REFERENCES hospital(HospitalId);

ALTER TABLE blood_transfusion
ADD FOREIGN KEY (EmployeeId) REFERENCES hospital_employee(EmployeeId),
ADD FOREIGN KEY (RecipientId) REFERENCES client(ClientId);

ALTER TABLE blood_donation
ADD FOREIGN KEY (EmployeeId) REFERENCES hospital_employee(EmployeeId),
ADD FOREIGN KEY (DonorId) REFERENCES client(ClientId);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;