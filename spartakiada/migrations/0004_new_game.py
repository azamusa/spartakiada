# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0003_auto_20170216_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=200)),
            ],
        ),
    ]
