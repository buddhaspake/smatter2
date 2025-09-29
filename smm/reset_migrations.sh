#!/bin/bash

# Remove migrations from added apps
# base app
rm -f base/migrations/00*.py
rm -rf base/migrations/__pycache__
# research app
rm -f research/migrations/00*.py
rm -rf research/migrations/__pycache__

# Remove migrations from home app, except first 3
# These are core wagtails migrations we need to keep
find home/migrations/ -regex ".+/000[^1-3].+\.py" -exec rm  {} \;
rm -rf home/migrations/__pycache__

# Backup database w/ timestamp if it exists
mkdir -p ../../db_backups/
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
target_path="../../db_backups/db_$timestamp.sqlite3"
if [ -f db.sqlite3 ]; then
    mv db.sqlite3 $target_path
fi

# Make migrations
python ./manage.py makemigrations
python ./manage.py migrate

# Create Django superuser
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL="da.animator@gmail.com"
python ./manage.py createsuperuser --noinput

