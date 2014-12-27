# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0002_publication_show'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line',
            old_name='h',
            new_name='b',
        ),
        migrations.RenameField(
            model_name='line',
            old_name='w',
            new_name='l',
        ),
        migrations.RenameField(
            model_name='line',
            old_name='x',
            new_name='r',
        ),
        migrations.RenameField(
            model_name='line',
            old_name='y',
            new_name='t',
        ),
    ]
