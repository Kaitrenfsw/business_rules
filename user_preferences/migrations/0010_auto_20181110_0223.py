# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-10 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_preferences', '0009_auto_20181027_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('new_id', models.CharField(max_length=100)),
                ('vote', models.IntegerField()),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='user_preferences.Source')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='uservote',
            unique_together=set([('user_id', 'new_id')]),
        ),
    ]
