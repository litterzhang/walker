# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20160417_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='detail',
            field=models.CharField(blank=True, default='标记详情', max_length=200),
        ),
        migrations.AddField(
            model_name='marker',
            name='name',
            field=models.CharField(blank=True, default='标记点', max_length=50),
        ),
    ]
