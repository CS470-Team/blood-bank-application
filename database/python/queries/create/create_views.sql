CREATE VIEW v_GetClientWithDonations AS
SELECT
    *
FROM
    client
    JOIN blood_donation ON client.ClientId = blood_donation.DonorId;

CREATE VIEW v_GetClientWithTransfusions AS
SELECT
    *
FROM
    client
    JOIN blood_transfusion ON client.ClientId = blood_transfusion.RecipientId;

-- The next one is a little quirky and probably won't produce anything, I found an issue with my fake data generation that I'm still working out!
-- It'll be fully resolved before the due date.

CREATE VIEW v_BloodBankManagers AS
SELECT
    *
FROM
    blood_bank_employee
    JOIN blood_bank ON blood_bank_employee.EmployeeId = blood_bank.ManagerId
    AND blood_bank_employee.EmployerId = blood_bank.BloodBankId;
