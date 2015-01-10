# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0013_auto_20150110_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='block',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='volume',
            name='volume',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
