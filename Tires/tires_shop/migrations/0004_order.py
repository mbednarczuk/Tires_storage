# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-19 09:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tires_shop', '0003_brandsdescribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=5)),
                ('order_tire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tires_shop.Tires', verbose_name='order_tire')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
