# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('w', models.IntegerField()),
                ('h', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('year', models.CharField(max_length=4)),
                ('summary', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='publication',
            field=models.ForeignKey(to='pubs.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='line',
            name='page',
            field=models.ForeignKey(to='pubs.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='publication',
            field=models.ForeignKey(to='pubs.Publication'),
            preserve_default=True,
        ),
    ]
