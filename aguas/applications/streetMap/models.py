from django.db import models



class CommunityAgency(models.Model):
    name_CA = models.CharField('Administrador de fincas', max_length=20, null=True, blank=True)
    address_CA = models.CharField('Dirección', max_length=100, null=True, blank=True)
    phone1_CA = models.CharField('Teléfono1', max_length=12, null=True, blank=True)
    phone2_CA = models.CharField('Teléfono2', max_length=12, null=True, blank=True)
    email_CA = models.EmailField('Email', max_length=30, null=True, blank=True)
    info_CA = models.TextField('Observaciones', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Administrador de Fincas'
        verbose_name_plural = 'Administradores de Fincas'
        ordering = ['name_CA']

    def __str__(self):
        return self.name_CA

class Contact(models.Model):
    name_contact = models.CharField('Nombre', max_length=20, null=True, blank=True)
    lastname_contact = models.CharField('Apellido', max_length=20, null=True, blank=True)
    phone1_contact = models.CharField('Teléfono1', max_length=20,null=True, blank=True)
    phone2_contact = models.CharField('Teléfono2', max_length=20, null=True, blank=True)
    email_contact = models.EmailField('Email', max_length=40, null=True, blank=True)
    detail_contact = models.TextField('Detalles del contacto', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['lastname_contact']

    def __str__(self):
        return self.name_contact + '' + self.phone1_contact

class StreetMap(models.Model):
    name = models.CharField('Nombre',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Calle'
        verbose_name_plural = 'Calles'
        ordering = ['name']

    def __str__(self):
        return self.name


class Address(models.Model):
    street_Address = models.ForeignKey(StreetMap, on_delete=models.CASCADE,null=True, blank=True)
    number_Address = models.CharField('Número calle', max_length=20)
    contact_Address = models.ManyToManyField(Contact)
    communityAgency_Address = models.ManyToManyField(CommunityAgency)

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
        ordering = ['number_Address']

    def __str__(self):
        return  str(self.street_Address) + '' + str(self.number_Address)




