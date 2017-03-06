# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20170306_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dni',
            field=models.CharField(max_length=255, unique=True, verbose_name=b'DNI'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name=b'email'),
        ),
    ]