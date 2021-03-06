# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-27 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doniServer', '0011_auto_20161225_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='BpLocation',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('bp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doniServer.BpBasic')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bp_location_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bp_location_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bp_location',
            },
        ),
        migrations.CreateModel(
            name='UserContactNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=100)),
                ('extension', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doniServer.BpBasic')),
                ('contact_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doniServer.ContactType')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contact_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_contact_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_contact_number',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doniServer.Designation'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_messages',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_new_transaction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_shipment_arrival',
            field=models.BooleanField(default=False),
        ),
    ]
