from model import *

def write_sql_insert(entity):
    sql = entity.generate_sql_insert()
    filename, _ = dataclass_fields(entity)
    with open(f"queries/insert/{snake_case(filename)}.sql", 'w') as f:
        f.write(sql)

if __name__ == "__main__":
    for entity in [
        Client, BloodBank, BloodBankEmployee, Hospital,
        HospitalEmployee, BloodTransfusion, BloodDonation
    ]:
        write_sql_insert(entity)
    