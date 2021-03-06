# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170716_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_pid', models.CharField(max_length=255)),
                ('to_pid', models.CharField(max_length=255)),
                ('reminder_time', models.TimeField()),
                ('from_text', models.CharField(max_length=255)),
                ('to_text', models.CharField(max_length=255)),
            ],
        ),
    ]
