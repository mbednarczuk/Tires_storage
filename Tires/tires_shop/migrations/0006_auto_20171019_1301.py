# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-19 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tires_shop', '0005_auto_20171019_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandsdescribe',
            name='brand_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='tires',
            name='tire_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires_shop.BrandsDescribe'),
        ),
    ]
