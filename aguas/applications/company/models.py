from django.db import models

# Create your models here.
class Company(models.Model):
    name_company = models.CharField('Nombre',max_length=50,null=True, blank=True)
    vat_company = models.CharField('Numero de indentificación fiscal',max_length=50,null=True, blank=True)
    
    class Meta:
        verbose_name = 'Compañía'
        verbose_name_plural = 'Compañías'
        ordering = ['name_company']

    def __str__(self):
        return str(self.name_company)

class Email(models.Model):
    address_email = models.CharField('Email',max_length=60,null=True, blank=True)
    description_email = models.CharField('Descripción',max_length=60,null=True, blank=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Email'
        ordering = ['address_email']

    def __str__(self):
        return str(self.address_email)
