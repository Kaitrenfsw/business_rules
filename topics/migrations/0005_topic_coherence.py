# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-22 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20180918_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='coherence',
            field=models.FloatField(default=0.5),
        ),
    ]
