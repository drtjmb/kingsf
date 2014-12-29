# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0006_auto_20141229_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='has_fulltext',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
