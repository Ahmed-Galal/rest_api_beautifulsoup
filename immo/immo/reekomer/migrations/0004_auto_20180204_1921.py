# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reekomer', '0003_edition_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='code_postal',
            field=models.CharField(max_length=100, verbose_name='Code Postal'),
        ),
        migrations.AlterField(
            model_name='region',
            name='date',
            field=models.CharField(max_length=100, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='region',
            name='idannonce',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='region',
            name='phone_number',
            field=models.CharField(max_length=100, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='region',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Prix'),
        ),
        migrations.AlterField(
            model_name='region',
            name='price_msquare',
            field=models.CharField(max_length=100, verbose_name='Prix m2'),
        ),
        migrations.AlterField(
            model_name='region',
            name='size',
            field=models.CharField(max_length=100, verbose_name='M2'),
        ),
    ]
