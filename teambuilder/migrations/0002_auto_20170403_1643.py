# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='userid',
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]