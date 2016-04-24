
# TODO


    django-admin.py startproject djangostructlog
    cd djangostructlog
    python manage.py startapp structlog

    python manage.py makemigrations --empty structlog # for 0001 initial...

    python manage.py migrate

    python manage.py makemigrations
    python manage.py migrate








    from structlog.models import LogItem
    LogItem.objects.filter(attributes__has_key='time_s')



http://stackoverflow.com/questions/26415113/how-can-i-change-the-returned-value-of-a-field-in-a-queryset-based-on-some-passe

