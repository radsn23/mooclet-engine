# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20170628_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
