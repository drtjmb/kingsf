# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0003_auto_20141227_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='publication',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='show',
            new_name='indexed',
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
