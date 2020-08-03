web: python manage.py runserver 0.0.0.0:5000
web: sudo rabbitmqctl add_user myuser mypassword
web: sudo rabbitmqctl add_vhost myvhost
web: sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
web: celery -A acme worker -l info