from random import choice, choices, randint, sample
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
    def generate_sql_insert(cls):
        """this is gross and i'm sure there's a better way"""
        fake_values = cls.random_list(cls.count())
        name, fields = dataclass_fields(cls)
        camel_case_fields = [camel_case(field) for field in fields]
        sql = f"INSERT INTO {name} ({', '.join(camel_case_fields)}) VALUES\n"
        for value in fake_values:
            sql += "\t("
            typed_values = [ty(val) for ty, val in value_tuple(value, fields)]
            for typed_value in typed_values:
                if type(typed_value) is str:
                    typed_value = f"'{typed_value}'"
                sql += f"{typed_value}, "
            sql = sql[:-2] + "),\n"
        sql = sql[:-2] + ";"
        return sql

    @staticmethod
    @abstractmethod
    def count() -> int:
        pass

    @classmethod
    @abstractmethod
    def random(cls, count):
        pass

    @classmethod
    def random_list(cls, n: int) -> List:
        return [cls.random() for i in range(n)]


def snake_case(name):
    return sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def camel_case(name):
    return "".join(word.title() for word in name.split("_"))


def dataclass_fields(dataclass):
    name = snake_case(dataclass.__name__)
    return name, [f.name for f in fields(dataclass)]


def generate_fake_address():
    with open("street_names.txt") as f:
        street_name = choice(list(map(lambda x: x.title(), f.read().splitlines())))
        return f"{randint(1, 1000)} {choice('NSEW')} {street_name}"


def generate_fake_name():
    with open("first_names.txt") as f:
        first_names = f.read().replace("'", "").splitlines()
    with open("last_names.txt") as f:
        last_names = f.read().replace("'", "").splitlines()
    return f"{choice(first_names)} {choice(last_names)}"


def generate_fake_phone():
    return f"{randint(100, 999):03}-{randint(100, 999):03}-{randint(1000, 9999):04}"


def generate_fake_password():
    salt = bcrypt.gensalt(4)
    hash = bcrypt.hashpw(str(randint(0, 1000000)).encode(), salt)
    return (salt.decode("utf-8"), hash.decode("utf-8"))


def generate_fake_date(year_range=(1930, 2000)):
    return f"{randint(year_range[0], year_range[1]):04}-{randint(1, 12):02}-{randint(1, 28):02}"


def generate_fake_birthday():
    return generate_fake_date(year_range=(1930, 2000))


def generate_fake_donation_date():
    return generate_fake_date(year_range=(2015, 2022))


def generate_fake_ssn():
    return randint(1000000, 9999999)


@dataclass
class Client(Entity):
    full_name: str
    blood_type: str
    email_address: str
    home_address: str
    date_of_birth: str
    phone_number: str
    password_salt: str
    password_hash: str

    @staticmethod
    def count() -> int:
        return 100

    @classmethod
    def random(cls) -> "Client":
        name = generate_fake_name()
        salt, hash = generate_fake_password()
        return cls(
            full_name=name,
            blood_type=choice(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]),
            email_address=f"{name}@gmail.com",
            home_address=generate_fake_address(),
            date_of_birth=generate_fake_birthday(),
            phone_number=generate_fake_phone(),
            password_salt=salt,
            password_hash=hash,
        )


@dataclass
class BloodDonation(Entity):
    employee_id: int
    donor_id: int
    screen_result: str
    donation_date: str
    amount: int

    @staticmethod
    def count() -> int:
        return 200

    @classmethod
    def random(cls) -> "BloodDonation":
        return cls(
            employee_id=randint(0, BloodBankEmployee.count() - 1),
            donor_id=randint(0, Client.count()),
            screen_result=choice(["positive", "negative"]),
            donation_date=generate_fake_donation_date(),
            amount=randint(0, Client.count()),
        )


@dataclass
class BloodTransfusion(Entity):
    employee_id: str
    transfusion_date: str
    amount: int
    recipient_id: int

    @staticmethod
    def count() -> int:
        return 200

    @classmethod
    def random(cls) -> "BloodTransfusion":
        return cls(
            employee_id=randint(0, BloodBankEmployee.count()),
            transfusion_date=generate_fake_donation_date(),
            amount=randint(1, 5),
            recipient_id=randint(0, Client.count()),
        )


@dataclass
class Hospital(Entity):
    hospital_name: str
    street_address: str

    @staticmethod
    def count() -> int:
        return 3

    @classmethod
    def random(cls, name: str) -> "Hospital":
        return cls(
            hospital_name=name,
            street_address=generate_fake_address(),
        )

    @classmethod
    def random_list(cls, n: int) -> "Hospital":
        hospital_names = ["Hospital A", "Hospital B", "Hospital C"]
        return [
            cls(hospital_names[i], street_address=generate_fake_address())
            for i in range(n)
        ]


@dataclass
class HospitalEmployee(Entity):
    employer_id: int
    full_name: str

    @staticmethod
    def count() -> int:
        return 50

    @classmethod
    def random(cls) -> "HospitalEmployee":
        return cls(
            employer_id=randint(0, Hospital.count()),
            full_name=generate_fake_name(),
        )


@dataclass
class BloodBank(Entity):
    manager_id: int
    street_address: int

    @staticmethod
    def count() -> int:
        return 10

    @classmethod
    def random(cls, manager_id: int) -> "BloodBank":
        return cls(
            manager_id,
            street_address=generate_fake_address(),
        )

    @classmethod
    def random_list(cls, n: int) -> List:
        manager_ids = sample(range(1, BloodBankEmployee.count()), k=n)
        return [cls.random(manager_ids[i]) for i in range(n)]


@dataclass
class BloodBankEmployee(Entity):
    employer_id: int
    full_name: str
    date_of_birth: str
    ssn: int
    password_salt: str
    password_hash: str
    home_address: str
    phone_number: str

    @staticmethod
    def count() -> int:
        return 100

    @classmethod
    def random(cls) -> "BloodBankEmployee":
        name = generate_fake_name()
        salt, hash = generate_fake_password()
        return cls(
            employer_id=randint(0, BloodBank.count()),
            full_name=name,
            date_of_birth=generate_fake_birthday(),
            ssn=generate_fake_ssn(),
            password_salt=salt,
            password_hash=hash,
            home_address=generate_fake_address(),
            phone_number=generate_fake_phone(),
        )
