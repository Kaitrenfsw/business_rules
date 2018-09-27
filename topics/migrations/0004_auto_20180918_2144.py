# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-18 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20180918_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='lda_model',
        ),
        migrations.AddField(
            model_name='topic',
            name='lda_model_id',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
