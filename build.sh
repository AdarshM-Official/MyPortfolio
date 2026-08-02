#!/usr/bin/env bash
# exit on error
set -o errexit

python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python manage.py collectstatic --no-input
venv/bin/python manage.py migrate