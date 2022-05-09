#!/bin/bash

# Allow external hosts (us via Docker) to connect to the database
mysql -uroot -proot -e "UPDATE mysql.user SET host = '%' WHERE user='root';"

# Drop tables before re-creating them

echo "Running scripts in queries/create..."
mysql -uroot -proot bloodbank < queries/delete/drop_tables.sql

# Run the table creation script

echo "Running scripts in queries/create..."
echo ">>> Running queries/create/create_tables.sql"
mysql -uroot -proot bloodbank < queries/create/create_tables.sql

for file in queries/create/*.sql; do
    echo ">>> Running $file"
    mysql -uroot -proot bloodbank < $file
done

# Run the demo-data insertion scripts

echo "Running scripts in queries/insert..."

for file in queries/insert/*.sql; do
    echo ">>> Running $file"
    mysql -uroot -proot bloodbank < $file
done

# Run the foreign key creation script

echo "Running queries/update/add_foreign_keys.sql"
mysql -uroot -proot bloodbank < queries/update/add_foreign_keys.sql