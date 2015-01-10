# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0012_auto_20150110_0903'),
        ('wp', '0002_boundingbox_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fulltext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('publication', models.ForeignKey(to='pubs.Publication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='normfulltext',
            name='publication',
        ),
        migrations.DeleteModel(
            name='NormFulltext',
        ),
        migrations.RemoveField(
            model_name='boundingbox',
            name='line',
        ),
        migrations.AddField(
            model_name='boundingbox',
            name='block',
            field=models.ForeignKey(default=1, to='pubs.Block'),
            preserve_default=False,
        ),
    ]
