# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
