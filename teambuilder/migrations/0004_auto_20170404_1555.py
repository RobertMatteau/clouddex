# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0003_auto_20170404_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='spattack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='spdefense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='speed',
            field=models.IntegerField(default=0),
        ),
    ]
