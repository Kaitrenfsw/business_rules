# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-23 00:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_preferences', '0007_auto_20181023_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicgraph',
            old_name='topic_id',
            new_name='topic_user_id',
        ),
    ]
