web: gunicorn acme.wsgi --workers 3 --timeout 120 --log-file -
worker: celery -A acme worker -l info