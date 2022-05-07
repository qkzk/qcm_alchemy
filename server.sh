#!/usr/bin/sh

gunicorn wsgi:app --config gunicorn_config.py
