# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0013_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='pors',
            field=models.CharField(max_length=10),
        ),
    ]
