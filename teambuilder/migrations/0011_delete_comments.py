# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0010_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
