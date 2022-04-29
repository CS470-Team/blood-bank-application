#!/bin/bash

# Allow external hosts (us via Docker) to connect to the database
mysql -uroot -proot -e "UPDATE mysql.user SET host = '%' WHERE user='root';"

# Drop tables before re-creating them
mysql -uroot -proot bloodbank < queries/delete/drop_tables.sql

# Run the table creation script
mysql -uroot -proot bloodbank < queries/create/create_tables.sql

# Run the demo-data insertion scripts
for f in queries/insert/*.sql; do
    echo "Running $f"
    mysql -uroot -proot bloodbank < $f
done

# Run the foreign key creation script
mysql -uroot -proot bloodbank < queries/update/add_foreign_keys.sql