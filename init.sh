python3 manage.py migrate
python3 manage.py collectstatic
export DJANGO_SUPERUSER_PASSWORD=$ADMIN_PASSWORD
python3 manage.py createsuperuser --username $ADMIN_USERNAME --noinput --email $ADMIN_EMAIL