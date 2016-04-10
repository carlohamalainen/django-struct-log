from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import HStoreField

class LogItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # e.g. 'rdiff-backup'
    name = models.CharField(max_length=200)

    # e.g. 'my-server-1'
    host = models.CharField(max_length=200)

    # e.g. 'carlo'
    user = models.CharField(max_length=200)

    # Maybe something nice for a graph or email subject line.
    # e.g. 'daily rdiff-backup of something'
    description = models.TextField()

    # key/value blob
    attributes = HStoreField()

    def __str__(self):
        return self.name
