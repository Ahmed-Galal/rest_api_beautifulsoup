# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_immo', models.CharField(default='', max_length=100)),
                ('numero', models.IntegerField()),
                ('rue', models.CharField(max_length=100)),
                ('intitule', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('code_postal', models.IntegerField(default='')),
                ('adresse', models.CharField(max_length=100)),
                ('surface', models.IntegerField()),
                ('sous_sol', models.IntegerField()),
                ('etages', models.IntegerField()),
                ('fai', models.NullBooleanField()),
                ('prix', models.IntegerField()),
                ('commission', models.CharField(max_length=100)),
                ('loyer', models.IntegerField()),
                ('loue', models.NullBooleanField(default='')),
                ('eof_bail', models.DateField()),
                ('date_entre', models.DateField(default='')),
                ('description', models.CharField(max_length=1000)),
                ('prix_m2', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('rentabilite', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('remb_moyen', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('interet', models.DecimalField(decimal_places=2, default='0', max_digits=19, null=True)),
                ('ecart', models.DecimalField(decimal_places=2, default='0', max_digits=19, null=True)),
                ('agence', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(max_length=200)),
                ('montant', models.IntegerField(null=True)),
                ('label', models.CharField(blank=True, max_length=100)),
                ('archive', models.CharField(blank=True, max_length=300)),
                ('vendu', models.CharField(blank=True, max_length=300)),
                ('achete', models.CharField(blank=True, max_length=300)),
                ('offre', models.CharField(blank=True, max_length=300)),
                ('date_offre', models.DateField(blank=True, default='', null=True)),
                ('file_upload', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Habitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('price', models.IntegerField(verbose_name='Prix')),
                ('code_postal', models.IntegerField(verbose_name='Code Postal')),
                ('price_msquare', models.IntegerField(verbose_name='Prix m2')),
                ('place', models.CharField(max_length=50, verbose_name='Lieu')),
                ('typeImo', models.CharField(max_length=100, verbose_name='Titre')),
                ('size', models.IntegerField(verbose_name='M2')),
                ('charac', models.CharField(max_length=100, verbose_name='Autre')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('link', models.CharField(max_length=300, unique=True, verbose_name='Lien')),
                ('website', models.CharField(max_length=100, verbose_name='Source')),
                ('image', models.CharField(max_length=100, verbose_name='Photo')),
                ('idannonce', models.IntegerField()),
                ('phone_number', models.IntegerField(verbose_name='Telephone')),
            ],
        ),
        migrations.CreateModel(
            name='Immeuble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('price', models.IntegerField(verbose_name='Prix')),
                ('code_postal', models.IntegerField(verbose_name='Code Postal')),
                ('price_msquare', models.IntegerField(verbose_name='Prix m2')),
                ('place', models.CharField(max_length=50, verbose_name='Lieu')),
                ('typeImo', models.CharField(max_length=100, verbose_name='Titre')),
                ('size', models.IntegerField(verbose_name='M2')),
                ('charac', models.CharField(max_length=100, verbose_name='Autre')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('link', models.CharField(max_length=300, unique=True, verbose_name='Lien')),
                ('website', models.CharField(max_length=100, verbose_name='Source')),
                ('image', models.CharField(max_length=100, verbose_name='Photo')),
                ('idannonce', models.IntegerField()),
                ('phone_number', models.IntegerField(verbose_name='Telephone')),
            ],
        ),
        migrations.CreateModel(
            name='Immo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('price', models.IntegerField(verbose_name='Prix')),
                ('code_postal', models.IntegerField(verbose_name='Code Postal')),
                ('place', models.CharField(max_length=50, verbose_name='Lieu')),
                ('typeImo', models.CharField(max_length=100, verbose_name='Titre')),
                ('size', models.IntegerField(verbose_name='M2')),
                ('charac', models.CharField(max_length=100, verbose_name='Autre')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('link', models.CharField(max_length=300, unique=True, verbose_name='Lien')),
                ('website', models.CharField(max_length=100, verbose_name='Source')),
                ('image', models.CharField(max_length=100, verbose_name='Photo')),
                ('idannonce', models.IntegerField()),
                ('phone_number', models.IntegerField(verbose_name='Telephone')),
                ('price_msquare', models.IntegerField(verbose_name='Prix M2')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('price', models.IntegerField(verbose_name='Prix')),
                ('code_postal', models.IntegerField(verbose_name='Code Postal')),
                ('price_msquare', models.IntegerField(verbose_name='Prix m2')),
                ('place', models.CharField(max_length=50, verbose_name='Lieu')),
                ('typeImo', models.CharField(max_length=100, verbose_name='Titre')),
                ('size', models.IntegerField(verbose_name='M2')),
                ('charac', models.CharField(max_length=100, verbose_name='Autre')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('link', models.CharField(max_length=300, unique=True, verbose_name='Lien')),
                ('website', models.CharField(max_length=100, verbose_name='Source')),
                ('image', models.CharField(max_length=100, verbose_name='Photo')),
                ('idannonce', models.IntegerField()),
                ('phone_number', models.IntegerField(verbose_name='Telephone')),
            ],
        ),
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telephone', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]