# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0005_auto_20160630_2158'),
        ('fridge_app', '0004_auto_20160630_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge_app.Fridge')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_app.User')),
            ],
        ),
    ]
