#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
echo Starting Gunicorn.
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --name {{ project_name }} \
    --workers 2 \
    --log-level=info \
"$@"
echo ohmmm
