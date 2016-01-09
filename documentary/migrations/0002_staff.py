# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=4)),
                ('photo', models.ImageField(null=True, upload_to=b'photo', blank=True)),
                ('birthday', models.DateTimeField()),
                ('join_time', models.DateTimeField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
