import mysql.connector

from model import BloodBankEmployee

class Database:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="0.0.0.0",    # for docker-compose
            port=3306,
            user="root",
            password="root",
            database="bloodbank",
        )
        self.cur = self.con.cursor()
        

    def populate_blood_bank_and_employees(self):
        values = [(1, 1, "101 1st Street"), (2, 2, "202 2nd Street"), (3, 3, "303 3rd Street")]
        # self.cur.execute("""""")
        self.cur.execute("""SET GLOBAL FOREIGN_KEY_CHECKS=0;""")
        
        self.cur.executemany(
            """INSERT INTO blood_bank (BloodBankID, ManagerID, StreetAddress) VALUES (%s, %s, %s)""", values
        )

        values = [(fake.blood_bank_id, fake.full_name, fake.date_of_birth, fake.ssn, fake.password_salt, fake.password_hash, fake.street_address, fake.phone_number) for fake in BloodBankEmployee.random_list(5)]
        self.cur.executemany("INSERT INTO blood_bank_employee (BloodBankID, FullName, DateOfBirth, SSN, PasswordSalt, PasswordHash, StreetAddress, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", values)

        self.cur.execute("""SET GLOBAL FOREIGN_KEY_CHECKS=0;""")
        self.con.commit()
        
if __name__ == "__main__":
    db = Database()
    db.populate_blood_bank_and_employees()
    # db.populate_blood_bank()