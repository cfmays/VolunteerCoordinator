# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-26 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='category',
            field=models.CharField(choices=[('C', 'Charity'), ('M', 'Commercial'), ('R', 'Religious')], default='C', max_length=2),
            preserve_default=False,
        ),
    ]
