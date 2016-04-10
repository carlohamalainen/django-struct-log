
# TODO


    django-admin.py startproject djangostructlog
    cd djangostructlog
    python manage.py startapp structlog


    sudo su - postgres

    createdb djangostructlog
    createuser structlog -s -P  # just for demo, set password to structlog

    psql djangostructlog

    # CREATE EXTENSION hstore;
    # GRANT ALL PRIVILEGES ON DATABASE djangostructlog TO structlog;
    # \q




    python manage.py makemigrations --empty structlog # for 0001 initial...

    python manage.py migrate

    python manage.py makemigrations
    python manage.py migrate

    python manage.py shell

    from django.contrib.auth.models import User
    User.objects.create_superuser(u'admin', u'admin@example.com', u'admin')
    from rest_framework.authtoken.models import Token

    for user in User.objects.all():
        t = Token.objects.get_or_create(user=user)
        print user, t

    admin (<Token: 5a610d074e24692c9084e6c845da39acc0ee0002>, True)



    curl \
        -H "Content-Type: application/json" \
        -H "Authorization: Token 5a610d074e24692c9084e6c845da39acc0ee0002" \
        -X POST \
        -d '{"name": "rdiff-backup", "host": "my-server-1", "description": "blah", "user": "carlo", "description": "daily rdiff-backup", "attributes": {"time_s": "1230"} }' \
        http://localhost:8000/logitems/


    {"name":"rdiff-backup","host":"my-server-1","user":"carlo","description":"daily rdiff-backup","attributes":{"time_s":"1230"},"created_at":"2016-04-10T14:47:31.393234Z","updated_at":"2016-04-10T14:47:31.393259Z"}✓ 10:47:31 carlo@e450 {master} ~/work/github/django-struct-log $ 





    from structlog.models import LogItem
    LogItem.objects.filter(attributes__has_key='time_s')



http://stackoverflow.com/questions/26415113/how-can-i-change-the-returned-value-of-a-field-in-a-queryset-based-on-some-passe

