#/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

$@

gunicorn locationstation.wsgi:application --bind 0.0.0.0:8000