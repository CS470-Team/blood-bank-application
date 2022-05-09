DELIMITER //

CREATE PROCEDURE `sp_GetTotalDonatedByClientId`(IN id INT)
BEGIN
    SELECT SUM(Amount)
    FROM blood_donation
    GROUP BY DonorId
    HAVING DonorId = id;
END //

CREATE PROCEDURE `sp_GetTotalReceivedByClientId`(IN id INT)
BEGIN
    SELECT SUM(Amount)
    FROM blood_transfusion
    GROUP BY RecipientId
    HAVING RecipientId = id;
END //

DELIMITER ;