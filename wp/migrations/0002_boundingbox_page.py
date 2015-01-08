# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundingbox',
            name='page',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
