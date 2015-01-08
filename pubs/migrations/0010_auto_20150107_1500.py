# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0009_auto_20150105_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='end_pos',
        ),
        migrations.RemoveField(
            model_name='line',
            name='start_pos',
        ),
        migrations.RemoveField(
            model_name='line',
            name='text_raw',
        ),
        migrations.AddField(
            model_name='line',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
