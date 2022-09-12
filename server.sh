#!/usr/bin/sh

gunicorn wsgi:app -w 3 --threads 1 -b 0.0.0.0:8000 --config gunicorn_hooks_config.py
# gunicorn wsgi:app --config gunicorn_config.py
