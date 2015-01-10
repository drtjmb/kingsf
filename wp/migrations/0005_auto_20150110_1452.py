# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wp', '0004_boundingbox_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boundingbox',
            name='end_pos',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='boundingbox',
            name='start_pos',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
