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
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seed', models.CharField(max_length=1024)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to='documentary.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_name', models.CharField(max_length=512)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='title',
            field=models.ForeignKey(to='documentary.Title'),
        ),
    ]
