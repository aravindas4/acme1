web: gunicorn mysite.wsgi --log-file
web: sudo rabbitmqctl add_user myuser mypassword
web: sudo rabbitmqctl add_vhost myvhost
web: sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
web: celery -A acme worker -l info