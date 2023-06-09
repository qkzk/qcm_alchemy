#!/usr/bin/sh

gunicorn wsgi:app -w 3 --threads 1 -b 0.0.0.0:443 --config gunicorn_hooks_config.py --access-logfile -
# gunicorn wsgi:app --config gunicorn_config.py
