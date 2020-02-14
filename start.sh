#!/bin/bash

echo "Creating Django migrations and seeding db..."
python manage.py makemigrations
python manage.py migrate
python manage.py seed_db --create-super-user

echo "Starting Django's development server..."
python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}