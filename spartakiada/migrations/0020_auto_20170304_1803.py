# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spartakiada', '0019_admin_f_s_sport_is'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_f_s',
            old_name='sport_is',
            new_name='sport_id',
        ),
    ]