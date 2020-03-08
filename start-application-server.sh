#!/bin/bash

echo "Applying migrations..."
python manage.py migrate

echo "Starting ASGI application with Daphne..."
daphne -b ${DJANGO_BIND_ADDRESS} -p ${DJANGO_BIND_PORT} django_chat.asgi:application