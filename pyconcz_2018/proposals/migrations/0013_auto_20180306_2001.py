# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0012_auto_20180306_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialaid',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='talk',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
    ]
