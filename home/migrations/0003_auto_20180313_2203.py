# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-13 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180312_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteriorDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Дизайн інтерєру',
                'verbose_name_plural': 'Дизайн інтерєру',
            },
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': 'Фото для слайдера', 'verbose_name_plural': 'Фото для слайдера'},
        ),
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.ImageField(upload_to='carousel_images/'),
        ),
    ]
