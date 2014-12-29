# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0004_auto_20141228_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='publication',
        ),
        migrations.AddField(
            model_name='line',
            name='publication',
            field=models.ForeignKey(default=None, to='pubs.Publication'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='line',
            name='page',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
