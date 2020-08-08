web: gunicorn acme.wsgi --threads 2 --worker-class gevent --workers 3 --timeout 120 --log-file -
worker: celery -A acme worker -l info