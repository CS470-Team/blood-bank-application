-- Two stored procedures with a simple SELECT to compare manually.

CALL sp_GetTotalDonatedByClientId(15);
SELECT * FROM blood_donation WHERE DonorId = 15;

CALL sp_GetTotalReceivedByClientId(15);
SELECT * FROM blood_transfusion WHERE RecipientId = 15;