#!/bin/bash

# Collect static files
echo "Collect static files"
/app/.venv/bin/python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
/app/.venv/bin/python manage.py migrate

# Start server
echo "Starting server"
/app/.venv/bin/python manage.py runserver 0.0.0.0:8000
