# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-14 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_topic_coherence'),
        ('user_preferences', '0003_auto_20180918_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TopicGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_graph', to='topics.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='UserGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_graph', to='user_preferences.GraphType')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_user', to='user_preferences.DashboardUser')),
            ],
        ),
        migrations.AddField(
            model_name='topicgraph',
            name='user_graph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graph_user', to='user_preferences.UserGraph'),
        ),
    ]
