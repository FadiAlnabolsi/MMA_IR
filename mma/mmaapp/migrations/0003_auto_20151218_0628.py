# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmaapp', '0002_auto_20151218_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighters',
            name='height',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='fighters',
            name='reach',
            field=models.CharField(max_length=3),
        ),
    ]
