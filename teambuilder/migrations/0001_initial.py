# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pors', models.BooleanField()),
                ('type', models.CharField(max_length=50)),
                ('power', models.IntegerField(default=0)),
                ('accuracy', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnum', models.IntegerField(default=0)),
                ('pname', models.CharField(max_length=50)),
                ('primarytype', models.CharField(max_length=50)),
                ('secondarytype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=200)),
                ('userid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamid', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
                ('pname', models.CharField(max_length=50)),
                ('pability', models.CharField(max_length=50)),
                ('pitem', models.CharField(max_length=50)),
                ('movea', models.CharField(max_length=50)),
                ('moveb', models.CharField(max_length=50)),
                ('movec', models.CharField(max_length=50)),
                ('moved', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
