# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-19 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateconversion',
            name='saturday_date',
            field=models.CharField(default='00/00/000', max_length=15),
        ),
    ]