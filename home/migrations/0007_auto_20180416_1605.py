# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-16 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_carousel_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='short_description',
        ),
        migrations.AddField(
            model_name='interiordesign',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
