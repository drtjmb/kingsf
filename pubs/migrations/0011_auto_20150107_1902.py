# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0010_auto_20150107_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='num_pages',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
