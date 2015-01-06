# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0008_auto_20150102_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='line',
        ),
        migrations.AddField(
            model_name='line',
            name='end_pos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='line',
            name='start_pos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='line',
            name='text_raw',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
