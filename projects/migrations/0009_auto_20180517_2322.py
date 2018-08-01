# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-17 20:22
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180416_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageprojectsdescription',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pageprojectsdescription',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pageprojectsdescription',
            name='sub_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
    ]
