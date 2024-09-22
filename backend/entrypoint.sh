#!/bin/sh

set -e

python scraper.py

cd /app

exec gunicorn backend:app --bind 0.0.0.0:5000 --workers 3
