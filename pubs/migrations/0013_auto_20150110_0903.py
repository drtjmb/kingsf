# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wp', '0003_auto_20150110_0903'),
        ('pubs', '0012_auto_20150110_0903'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Line',
        ),
        migrations.AddField(
            model_name='volume',
            name='publication',
            field=models.ForeignKey(to='pubs.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='volume',
            field=models.ForeignKey(to='pubs.Volume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='block',
            name='page',
            field=models.ForeignKey(to='pubs.Page'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='publication',
            name='has_fulltext',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='num_pages',
        ),
    ]
