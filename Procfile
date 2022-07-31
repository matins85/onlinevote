release: python3 manage.py migrate
web: daphne onlinevote.asgi:application --port $PORT --bind 0.0.0.0 -v2
# web: gunicorn onlinevote.wsgi --preload --log-file - --log-level debug
worker: python manage.py runworker --settings=onlinevote.settings -v2
# celery: celery -A onlinevote worker -l info --concurrency 2
# celerybeat: celery -A onlinevote worker -B -l info