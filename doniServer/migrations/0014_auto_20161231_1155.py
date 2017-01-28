# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-31 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doniServer', '0013_auto_20161227_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='notify_messages',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='businessLocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doniServer.BpLocation'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_daily_reports',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_monthly_reports',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_weekly_reports',
            field=models.BooleanField(default=True),
        ),
    ]
