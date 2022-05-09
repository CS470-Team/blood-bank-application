USE bloodbank;

START TRANSACTION;
SET FOREIGN_KEY_CHECKS=0; 

ALTER TABLE blood_bank_employee
ADD CONSTRAINT fk_employee_blood_bank_id FOREIGN KEY (EmployerId)
REFERENCES blood_bank(BloodBankId) ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE hospital_employee
ADD CONSTRAINT fk_employee_hospital_id FOREIGN KEY (EmployerId)
REFERENCES hospital(HospitalId) ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE blood_transfusion
ADD CONSTRAINT fk_transfusion_employee_id FOREIGN KEY (EmployeeId)
REFERENCES hospital_employee(EmployeeId) ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE blood_transfusion
ADD CONSTRAINT fk_transfusion_recipient_id FOREIGN KEY (RecipientId)
REFERENCES client(ClientId) ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE blood_donation
ADD CONSTRAINT fk_donation_employee_id FOREIGN KEY (EmployeeId)
REFERENCES blood_bank_employee(EmployeeId) ON DELETE RESTRICT
ON UPDATE CASCADE;

ALTER TABLE blood_donation
ADD CONSTRAINT fk_donation_donor_id FOREIGN KEY (DonorId)
REFERENCES client(ClientId) ON DELETE RESTRICT
ON UPDATE CASCADE;

SET FOREIGN_KEY_CHECKS=1;
COMMIT;