#!/bin/sh
set -e

echo "==> Waiting for database..."
python manage.py migrate --no-input 2>&1

echo "==> Collecting static files..."
python manage.py collectstatic --no-input 2>&1

echo "==> Starting Gunicorn on 0.0.0.0:8000 ..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --timeout 60 \
    --access-logfile - \
    --error-logfile -
