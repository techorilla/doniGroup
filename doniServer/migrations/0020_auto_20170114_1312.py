# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-14 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doniServer', '0019_auto_20170114_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='business',
            field=models.ForeignKey(default=1L, on_delete=django.db.models.deletion.CASCADE, to='doniServer.BpBasic'),
        ),
    ]
