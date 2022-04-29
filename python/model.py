from random import choice, randint
import random
from typing import List
import bcrypt
from dataclasses import dataclass, fields
from re import sub
from abc import ABC, abstractmethod

def value_tuple(value, fields) -> str:
    field_types = [type(getattr(value, field)) for field in fields]
    field_values = [str(getattr(value, field)) for field in fields]
    return list(zip(field_types, field_values))

class Entity(ABC):
    @classmethod
    def generate_sql_insert(cls, count):
        """this is gross and i'm sure there's a better way"""
        fake_values = cls.random_list(count)
        name, fields = dataclass_fields(cls)
        sql = f"INSERT INTO {name} ({', '.join(fields)}) VALUES\n"
        for value in fake_values:
            sql += "\t("
            typed_values = [ty(val) for ty, val in value_tuple(value, fields)]
            for typed_value in typed_values:
                if type(typed_value) is str:
                    typed_value = f"'{typed_value}'"
                sql += f"{typed_value}, "
            sql = sql[:-2] + '),\n'
        sql = sql[:-2] + ';'
        return sql
    
    @classmethod
    @abstractmethod
    def random(cls, count):
        pass

    @classmethod
    def random_list(cls, n: int) -> List:
        return [cls.random(i) for i in range(n)]
    
def camel_case(name):
  return sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def dataclass_fields(dataclass):
    name = camel_case(dataclass.__name__)
    return name, [f.name for f in fields(dataclass)]

def generate_fake_address():
    with open("street_names.txt") as f:
        street_name = choice(list(map(lambda x: x.title(), f.read().splitlines())))
        return f"{randint(1, 1000)} {choice('NSEW')} {street_name}"

def generate_fake_name():
    with open("first_names.txt") as f:
        first_names = f.read().replace("\'", "").splitlines()
    with open("last_names.txt") as f:
        last_names = f.read().replace("\'", "").splitlines()
    return f"{choice(first_names)} {choice(last_names)}"

def generate_fake_phone():
    return f"{randint(100, 999):03}-{randint(100, 999):03}-{randint(1000, 9999):04}"

def generate_fake_password():
    salt = bcrypt.gensalt(4)
    hash = bcrypt.hashpw(str(randint(0, 1000000)).encode(), salt)
    return (salt.decode('utf-8'), hash.decode('utf-8'))

def generate_fake_birthday():
    return f"{randint(1, 12)}/{randint(1, 28)}/{randint(1930, 2000)}"

def generate_fake_ssn():
    return f"{randint(100, 999):03}-{randint(0, 99):02}-{randint(0000, 9999):04}"

@dataclass
class Client(Entity):
    id: int
    full_name: str
    blood_type: str
    email_address: str
    street_address: str
    date_of_birth: str
    phone_number: str
    password_salt: str
    password_hash: str

    @classmethod
    def random(cls, id: int) -> "Client":
        name = generate_fake_name()
        salt, hash = generate_fake_password()
        return cls(
            id,
            full_name=name,
            blood_type=choice(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]),
            email_address=f"{name}@gmail.com",
            street_address=generate_fake_address(),
            date_of_birth=generate_fake_birthday(),
            phone_number=generate_fake_phone(),
            password_salt=salt,
            password_hash=hash,
        )

class BloodDonation(Entity):
    pass

class BloodTransfusion(Entity):
    pass

@dataclass
class Hospital(Entity):
    hospital_id: int
    hospital_name: str
    street_address: str
    
    @classmethod
    def random(cls, id: int) -> "Hospital":
        cls(
            id,
            hospital_name=choice(["Hospital A", "Hospital B", "Hospital C"]),
            street_address=generate_fake_address()
        )

@dataclass
class HospitalEmployee(Entity):
    employee_id: int
    hospital_id: int
    full_name: str
    
    @classmethod
    def random(cls, id: int) -> "HospitalEmployee":
        return cls(
            employee_id=id,
            hospital_id=randint(1, 2),
            full_name=generate_fake_name(),
        )
    
@dataclass
class BloodBank(Entity):
    blood_bank_id: int
    manager_id: int
    street_address: int

@dataclass
class BloodBankEmployee(Entity):
    employee_id: int
    blood_bank_id: int
    full_name: str
    date_of_birth: str
    ssn: int
    password_salt: str
    password_hash: str
    street_address: str
    phone_number: str
    
    @classmethod
    def random(cls, id) -> "BloodBankEmployee":
        name = generate_fake_name()
        salt, hash = generate_fake_password()
        return cls(
            employee_id=id,
            blood_bank_id=randint(0, 10),
            full_name=name,
            date_of_birth=generate_fake_birthday(),
            ssn=generate_fake_ssn(),
            password_salt=salt,
            password_hash=hash,
            street_address=generate_fake_address(),
            phone_number=generate_fake_phone(),
        )