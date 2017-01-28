# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 21:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import doniServer.models.businessPartner.bpProducts


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doniServer', '0002_usersession'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsSpecification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('moisture', models.FloatField(default=None, null=True)),
                ('purity', models.FloatField(default=None, null=True)),
                ('weaveled', models.FloatField(default=None, null=True)),
                ('splits', models.FloatField(default=None, null=True)),
                ('damaged', models.FloatField(default=None, null=True)),
                ('foreignMatter', models.FloatField(default=None, null=True)),
                ('greenDamaged', models.FloatField(default=None, null=True)),
                ('otherColor', models.FloatField(default=None, null=True)),
                ('wrinkled', models.FloatField(default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specs_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'product_specs',
            },
        ),
        migrations.RemoveField(
            model_name='products',
            name='damaged',
        ),
        migrations.RemoveField(
            model_name='products',
            name='foreignMatter',
        ),
        migrations.RemoveField(
            model_name='products',
            name='greenDamaged',
        ),
        migrations.RemoveField(
            model_name='products',
            name='moisture',
        ),
        migrations.RemoveField(
            model_name='products',
            name='otherColor',
        ),
        migrations.RemoveField(
            model_name='products',
            name='purity',
        ),
        migrations.RemoveField(
            model_name='products',
            name='splits',
        ),
        migrations.RemoveField(
            model_name='products',
            name='weaveled',
        ),
        migrations.RemoveField(
            model_name='products',
            name='wrinkled',
        ),
        migrations.AddField(
            model_name='bpproducts',
            name='prod_image',
            field=models.ImageField(blank=True, null=True, upload_to=doniServer.models.businessPartner.bpProducts.get_image_path),
        ),
        migrations.AddField(
            model_name='transaction',
            name='quality',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='doniServer.ProductKeyword'),
        ),
        migrations.RemoveField(
            model_name='products',
            name='origin',
        ),
        migrations.AddField(
            model_name='products',
            name='origin',
            field=models.ManyToManyField(related_name='origin', to='doniServer.Origin'),
        ),
        migrations.AddField(
            model_name='products',
            name='specification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doniServer.ProductsSpecification'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='specification',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='doniServer.ProductsSpecification'),
        ),
    ]
