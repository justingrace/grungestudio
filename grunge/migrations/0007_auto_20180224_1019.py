# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-24 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grunge', '0006_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(max_length=500, upload_to=b''),
        ),
    ]
