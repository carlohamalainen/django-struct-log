# django-struct-log

A simple Django app for distributed structured logging.

## Quickstart

Install Postgresql (Debian-like systems):

    $ sudo apt install postgresql                 \
                       postgresql-9.4             \
                       postgresql-client-9.4      \
                       postgresql-client-common   \
                       postgresql-common          \
                       postgresql-contrib-9.4     \
                       postgresql-server-dev-9.4  \
                       postgresql-server-dev-all

Pop into the Postgresql user:

    $ sudo su - postgres

and create a database for the app:

    $ createdb djangostructlog
    $ createuser structlog -s -P  # just for demo, set password to structlog

Now turn on the hstore extension:

    $ psql djangostructlog

    # CREATE EXTENSION hstore;
    # GRANT ALL PRIVILEGES ON DATABASE djangostructlog TO structlog;
    # \q

Clone the repo and run the migrations:

    git clone https://github.com/carlohamalainen/django-struct-log.git
    cd django-struct-log
    python manage.py migrate

Create the admin user and an auth token:

    python manage.py shell

    >>> from django.contrib.auth.models import User
    >>> from rest_framework.authtoken.models import Token

    >>> User.objects.create_superuser(u'admin', u'admin@example.com', u'admin')

    >>> for user in User.objects.all():
    >>>     t = Token.objects.get_or_create(user=user)
    >>>     print user, t

Make note of the auth token, e.g.:

    admin (<Token: 5a610d074e24692c9084e6c845da39acc0ee0002>, True)

Run the server:

    python manage.py runserver

Test a post to the server:

    curl                                                                    \
        -H "Content-Type: application/json"                                 \
        -H "Authorization: Token 5a610d074e24692c9084e6c845da39acc0ee0002"  \
        -X POST                                                             \
        -d '{"name": "rdiff-backup", "host": "my-server-1", "description": "blah", "user": "carlo", "description": "daily rdiff-backup", "attributes": {"time_s": "1230"} }' \
        http://localhost:8000/logitems/

The response should be something like:

    {"name":"rdiff-backup",
     "host":"my-server-1",
     "user":"carlo",
     "description":"daily rdiff-backup",
     "attributes":{"time_s":"1230"},
     "created_at":"2016-04-10T14:47:31.393234Z",
     "updated_at":"2016-04-10T14:47:31.393259Z"}


