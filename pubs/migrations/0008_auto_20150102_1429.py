# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0007_publication_has_fulltext'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='num_pages',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='featured',
            field=models.BooleanField(default=False, verbose_name=b'include in carousel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='has_fulltext',
            field=models.BooleanField(default=False, verbose_name=b'include in search results'),
            preserve_default=True,
        ),
    ]
