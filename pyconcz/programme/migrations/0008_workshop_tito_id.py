# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0007_auto_20190415_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='tito_id',
            field=models.SlugField(blank=True, help_text='Tickets are called releases in API', null=True, verbose_name='Ticket ID in ti.to'),
        ),
    ]
