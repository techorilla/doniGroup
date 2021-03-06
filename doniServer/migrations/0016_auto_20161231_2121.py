# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-31 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import doniServer.models.authentication.userProfile


class Migration(migrations.Migration):

    dependencies = [
        ('doniServer', '0015_userprofile_notify_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=doniServer.models.authentication.userProfile.get_image_path),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='small_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=doniServer.models.authentication.userProfile.get_image_path),
        ),
    ]
