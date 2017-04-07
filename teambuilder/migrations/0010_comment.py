# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0009_auto_20170405_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('teamid', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=600)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
