# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-25 09:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0031_auto_20170425_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='user_f_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
