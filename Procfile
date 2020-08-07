web: gunicorn acme.wsgi --worker-class gevent --workers 10 --timeout 120 --log-file -
worker: celery -A acme worker -l info