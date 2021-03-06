# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 22:05
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='band_name',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fav_color',
            field=colorful.fields.RGBColorField(blank=True, default='#5DADE2'),
        ),
    ]
