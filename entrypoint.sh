#!/bin/bash

echo "Collect static files"
.venv/bin/python manage.py collectstatic --noinput

echo "Apply database migrations"
.venv/bin/python manage.py migrate

echo "Starting server"
.venv/bin/python manage.py runserver 0.0.0.0:8012
