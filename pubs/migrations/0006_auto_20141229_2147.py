# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0005_auto_20141229_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='indexed',
        ),
        migrations.AddField(
            model_name='line',
            name='line',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
