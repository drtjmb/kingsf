# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0013_auto_20150110_0903'),
        ('wp', '0003_auto_20150110_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundingbox',
            name='publication',
            field=models.ForeignKey(default=1, to='pubs.Publication'),
            preserve_default=False,
        ),
    ]
