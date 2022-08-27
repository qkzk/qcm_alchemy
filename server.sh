#!/usr/bin/sh

gunicorn wsgi:app -w 3 --threads 1 -b 0.0.0.0:8000
# gunicorn wsgi:app --config gunicorn_config.py
