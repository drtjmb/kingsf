# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wp', '0005_auto_20150110_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boundingbox',
            name='page',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
