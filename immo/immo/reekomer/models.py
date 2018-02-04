# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class Habitation(models.Model):
    date = models.DateTimeField(verbose_name= 'Date')
    price = models.IntegerField(verbose_name= 'Prix')
    code_postal = models.IntegerField(verbose_name= 'Code Postal')
    price_msquare = models.IntegerField(verbose_name= 'Prix m2')
    place = models.CharField(max_length=50,verbose_name= 'Lieu')
    typeImo = models.CharField(max_length=100,verbose_name= 'Titre')
    size = models.IntegerField(verbose_name= 'M2')
    charac = models.CharField(max_length=100,verbose_name= 'Autre')
    description = models.CharField(max_length=1000,verbose_name= 'Description')
    link = models.CharField(max_length=300,unique=True,verbose_name= 'Lien')
    website = models.CharField(max_length=100,verbose_name= 'Source')
    image = models.CharField(max_length=100,verbose_name= 'Photo')
    idannonce = models.IntegerField()
    phone_number = models.IntegerField(verbose_name= 'Telephone')
    def save(self, *args, **kwargs):
        try:
            self.price_msquare = self.price/self.size
        except:
            self.price_msquare = 0
        return super(Habitation, self).save(*args, **kwargs)

# Create your models here.
class Edition(models.Model):
    type_immo = models.CharField(max_length=100,default='')
    numero = models.IntegerField()
    rue = models.CharField(max_length=100)
    intitule = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    code_postal = models.IntegerField(default='')
    adresse = models.CharField(max_length=100)
    surface = models.IntegerField()
    sous_sol = models.IntegerField()
    etages = models.IntegerField()
    fai = models.NullBooleanField(null=True, blank=True)
    prix = models.IntegerField()
    commission = models.CharField(max_length=100)
    loyer = models.IntegerField()
    loue = models.NullBooleanField(default='')
    eof_bail = models.DateField()
    date_entre = models.DateField(default='')
    description = models.CharField(max_length=1000)
    prix_m2 = models.DecimalField(null=True, max_digits=19, decimal_places=2)
    rentabilite = models.DecimalField(null=True, max_digits=19, decimal_places=2)
    remb_moyen = models.DecimalField(null=True, max_digits=19, decimal_places=2)
    interet = models.DecimalField(null=True, max_digits=19, decimal_places=2, default='0')
    ecart = models.DecimalField(null=True, max_digits=19, decimal_places=2, default='0')
    agence = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=200)
    montant = models.IntegerField(null=True)
    label = models.CharField(max_length=100, blank=True)
    archive = models.CharField(max_length=300, blank=True)
    vendu = models.CharField(max_length=300, blank=True)
    achete = models.CharField(max_length=300, blank=True)
    offre = models.CharField(max_length=300, blank=True)
    date_offre = models.DateField(default='', null=True, blank=True)
    file_upload = models.FileField(null=True, blank=True)

    def __str__(self):
        return ('{}').format(self.name)

    def get_absolute_url(self):
        return u'/bien/%d' % self.id


# Create your models here.
class Immeuble(models.Model):
    date = models.DateTimeField(verbose_name= 'Date')
    price = models.IntegerField(verbose_name= 'Prix')
    code_postal = models.IntegerField(verbose_name= 'Code Postal')
    price_msquare = models.IntegerField(verbose_name= 'Prix m2')
    place = models.CharField(max_length=50,verbose_name= 'Lieu')
    typeImo = models.CharField(max_length=100,verbose_name= 'Titre')
    size = models.IntegerField(verbose_name= 'M2')
    charac = models.CharField(max_length=100,verbose_name= 'Autre')
    description = models.CharField(max_length=1000,verbose_name= 'Description')
    link = models.CharField(max_length=300,unique=True,verbose_name= 'Lien')
    website = models.CharField(max_length=100,verbose_name= 'Source')
    image = models.CharField(max_length=100,verbose_name= 'Photo')
    idannonce = models.IntegerField()
    phone_number = models.IntegerField(verbose_name= 'Telephone')
    def save(self, *args, **kwargs):
        try:
            self.price_msquare = self.price/self.size
        except:
            self.price_msquare = 0
        return super(Immeuble, self).save(*args, **kwargs)


# Create your models here.
class Immo(models.Model):
    date = models.DateTimeField(verbose_name= 'Date')
    price = models.IntegerField(verbose_name= 'Prix')
    code_postal = models.IntegerField(verbose_name= 'Code Postal')
    place = models.CharField(max_length=50,verbose_name= 'Lieu')
    typeImo = models.CharField(max_length=100,verbose_name= 'Titre')
    size = models.IntegerField(verbose_name= 'M2')
    charac = models.CharField(max_length=100,verbose_name= 'Autre')
    description = models.CharField(max_length=1000,verbose_name= 'Description')
    link = models.CharField(max_length=300,unique=True,verbose_name= 'Lien')
    website = models.CharField(max_length=100,verbose_name= 'Source')
    image = models.CharField(max_length=100,verbose_name= 'Photo')
    idannonce = models.IntegerField()
    phone_number = models.IntegerField(verbose_name= 'Telephone')
    price_msquare = models.IntegerField(verbose_name= 'Prix M2')

    def save(self, *args, **kwargs):
        try:
            self.price_msquare = self.price/self.size
        except:
            self.price_msquare = 0
        return super(Immo, self).save(*args, **kwargs)

class Send(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.IntegerField()
    message = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.typeImo

# Create your models here.
class Region(models.Model):
    date = models.CharField(max_length=100,verbose_name= 'Date')
    price = models.CharField(max_length=100,verbose_name= 'Prix')
    code_postal = models.CharField(max_length=100,verbose_name= 'Code Postal')
    price_msquare = models.CharField(max_length=100,verbose_name= 'Prix m2')
    place = models.CharField(max_length=50,verbose_name= 'Lieu')
    typeImo = models.CharField(max_length=100,verbose_name= 'Titre')
    size = models.CharField(max_length=100,verbose_name= 'M2')
    charac = models.CharField(max_length=100,verbose_name= 'Autre')
    description = models.CharField(max_length=1000,verbose_name= 'Description')
    link = models.CharField(max_length=300,unique=True,verbose_name= 'Lien')
    website = models.CharField(max_length=100,verbose_name= 'Source')
    image = models.CharField(max_length=100,verbose_name= 'Photo')
    idannonce = models.CharField(max_length=100,)
    phone_number = models.CharField(max_length=100,verbose_name= 'Telephone')
    def save(self, *args, **kwargs):
        try:
            self.price_msquare = self.price/self.size
        except:
            self.price_msquare = 0
        return super(Region, self).save(*args, **kwargs)