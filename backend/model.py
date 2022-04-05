from random import choice, randint
from pydantic import BaseModel


class Client(BaseModel):
    pass

class BloodDonation(BaseModel):
    pass

class BloodTransfusion(BaseModel):
    pass

class Hospital(BaseModel):
    pass

class HospitalEmployee(BaseModel):
    pass

class BloodBank(BaseModel):
    def __init__(self,
        blood_bank_id: int,
        manager_id: int,
        street_address: int
    ):
        self.blood_bank_id = blood_bank_id
        self.manager_id = manager_id
        self.street_address = street_address


class BloodBankEmployee():
    def __init__(self,
            employee_id: int,
            blood_bank_id: int,
            full_name: str,
            date_of_birth: str,
            ssn: int,
            password_salt: str,
            password_hash: str,
            street_address: str,
            phone_number: str,
    ):
        self.employee_id = employee_id
        self.blood_bank_id = blood_bank_id
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.ssn = ssn
        self.password_salt = password_salt
        self.password_hash = password_hash
        self.street_address = street_address
        self.phone_number = phone_number

    @classmethod
    def random_list(cls, n: int):
        with open("first_names.txt") as f:
            first_names = f.readlines()
        with open("last_names.txt") as f:
            last_names = f.readlines()
        full_names = [f"{first_names[i].strip()} {last_names[i].strip()}" for i in range(n)]
        return [BloodBankEmployee(
            employee_id=i,
            blood_bank_id=randint(0, 3),
            full_name=f"{full_names[i]}",
            date_of_birth=f"{randint(1950, 1990)}-{randint(1, 12)}-{randint(1, 28)}",
            ssn=randint(100_00_0000, 900_00_0000),
            password_salt=f"salt{i}",
            password_hash=f"hash{i}",
            street_address=f"{randint(1, 100)} {random.choice(['North', 'West', 'East', 'South'])} {randint(1, 100)} St.",
            phone_number=f"{randint(100, 999)}-{randint(000, 999)}-{randint(000, 999)}",
        ) for i in range(n)]