# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-12 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
