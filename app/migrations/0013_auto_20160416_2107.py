# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_test_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='detail',
            field=models.CharField(default='暂无详情', max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='比赛房间', max_length=50),
        ),
    ]