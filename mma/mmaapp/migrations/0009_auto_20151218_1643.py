# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mmaapp', '0008_auto_20151218_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default=' Amway Center in Orlando, Florida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_day',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 16, 43, 28, 551323, tzinfo=utc)),
        ),
    ]
