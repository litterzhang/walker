# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160407_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
