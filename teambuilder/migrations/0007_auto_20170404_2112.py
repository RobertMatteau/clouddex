# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0006_auto_20170404_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={},
        ),
        migrations.AddField(
            model_name='team',
            name='comment',
            field=models.CharField(default='This team is terrible', max_length=600),
        ),
    ]