web: gunicorn acme.wsgi -threads 2 --workers 10 --timeout 120 --log-file -
worker: celery -A acme worker -l info