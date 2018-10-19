# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-19 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_preferences', '0004_auto_20181014_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicgraph',
            name='user_graph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics_selected', to='user_preferences.UserGraph'),
        ),
        migrations.AlterField(
            model_name='usergraph',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graphs_selected', to='user_preferences.DashboardUser'),
        ),
    ]
