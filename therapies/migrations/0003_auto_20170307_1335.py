# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapies', '0002_auto_20170307_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'ordering': ['terapy'], 'verbose_name': 'Hor\xe1rio'},
        ),
        migrations.AddField(
            model_name='time',
            name='seven',
            field=models.BooleanField(max_length=255, verbose_name=b'15:00-16:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='time',
            name='six',
            field=models.BooleanField(max_length=255, verbose_name=b'14:00-15:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='time',
            name='friday',
            field=models.BooleanField(max_length=255, verbose_name=b'6\xc2\xaa'),
        ),
        migrations.AlterField(
            model_name='time',
            name='monday',
            field=models.BooleanField(max_length=255, verbose_name=b'2\xc2\xaa'),
        ),
        migrations.AlterField(
            model_name='time',
            name='thursday',
            field=models.BooleanField(max_length=255, verbose_name=b'5\xc2\xaa'),
        ),
        migrations.AlterField(
            model_name='time',
            name='tuesday',
            field=models.BooleanField(max_length=255, verbose_name=b'3\xc2\xaa'),
        ),
        migrations.AlterField(
            model_name='time',
            name='wednesday',
            field=models.BooleanField(max_length=255, verbose_name=b'4\xc2\xaa'),
        ),
    ]