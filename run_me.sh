#!/bin/bash

python -m venv venv
source venv/bin/active
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

#DJANGO_SUPERUSER_USERNAME=admin \
#DJANGO_SUPERUSER_EMAIL=admin@example.com \
#DJANGO_SUPERUSER_PASSWORD=adminpassword \
#python manage.py createsuperuser --noinput

if [ -f db.sqlite3 ]; then
    echo "Database already exists"
else
    echo "Database does not, copying from backup"
    cp db_bak.sqlite3 db.sqlite3
fi

python manage.py runserver
