# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160417_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='creatorname',
            field=models.CharField(default='越野用户', max_length=50),
        ),
        migrations.AlterField(
            model_name='room_user',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room_user',
            name='isquit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='room_user',
            name='score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='room_user',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]