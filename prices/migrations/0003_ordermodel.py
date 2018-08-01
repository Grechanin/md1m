# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-20 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20180517_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(default=None, max_length=128)),
                ('client_name', models.CharField(default=None, max_length=128)),
                ('phone_number', models.CharField(default=None, max_length=128)),
                ('email', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
