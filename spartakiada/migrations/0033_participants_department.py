# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-25 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0032_auto_20170425_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spartakiada.User_f'),
        ),
    ]
