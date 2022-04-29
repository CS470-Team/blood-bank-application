from dataclasses import fields
from model import *

def write_sql_insert(entity, count):
    sql = entity.generate_sql_insert(count)
    filename, _ = dataclass_fields(entity)
    with open(f"../database/queries/insert/{filename}.sql", 'w') as f:
        f.write(sql)

if __name__ == "__main__":
    write_sql_insert(HospitalEmployee, 50)
    write_sql_insert(Client, 100)