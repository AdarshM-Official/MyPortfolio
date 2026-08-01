#!/usr/bin/env bash
# build_files.sh
echo "Building project..."
pip install -r requirements.txt
echo "Make migrations..."
python manage.py make_migrations
echo "Migrate..."
python manage.py migrate
echo "Collect static..."
python manage.py collectstatic --noinput --clear
echo "Build complete."
