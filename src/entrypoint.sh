#!/bin/bash
#
#python manage.py migrate >> /logs/log_manage.log 2>&1
#python manage.py collectstatic --noinput >> /logs/log_manage.log 2>&1
#
## run celery worker and schedular
#nohup celery -A app beat -l DEBUG >> /logs/log_celery_beat.log 2>&1 &
#nohup celery -A app worker -l DEBUG --concurrency 2 >> /logs/log_celery_worker.log 2>&1 &

# Start Django development server
exec "$@"
