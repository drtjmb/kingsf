# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0010_auto_20150107_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoundingBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('w', models.IntegerField()),
                ('h', models.IntegerField()),
                ('start_pos', models.IntegerField()),
                ('end_pos', models.IntegerField()),
                ('line', models.ForeignKey(to='pubs.Line')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NormFulltext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('publication', models.ForeignKey(to='pubs.Publication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('publication', models.ForeignKey(to='pubs.Publication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
