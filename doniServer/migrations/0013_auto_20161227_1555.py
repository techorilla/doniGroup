# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-27 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doniServer', '0012_auto_20161227_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='bplocation',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bplocation',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bplocation',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
