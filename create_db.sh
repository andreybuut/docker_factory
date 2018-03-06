#!/bin/bash

# this will ask you for password, use 'manager' - this is our default pass for postgis container
echo "Create new user: musicalbead_user"
echo "-------------------------------------------------------------------------------"
createuser -U postgres -h postgres -P -s -e musicalbead_user 

echo
echo "Create new db: musicalbead_dev"
echo "-------------------------------------------------------------------------------"
createdb -U musicalbead_user -h postgres  musicalbead_dev

echo
echo "Giving user standard password 'manager'"
echo "-------------------------------------------------------------------------------"
psql -U postgres -h postgres -c "ALTER USER musiaclbead_user WITH PASSWORD 'manager';"

echo
echo "Grant all privileges to the user on DB "
echo "-------------------------------------------------------------------------------"
psql -U postgres -h postgres -c "GRANT ALL PRIVILEGES ON DATABASE musicalbead_dev TO musicalbead_user;"

echo
echo "Installing postgis extension"
echo "-------------------------------------------------------------------------------"
psql -U postgres -h postgres -c "CREATE EXTENSION postgis;" musicalbead_dev
