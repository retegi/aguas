from django.db import models

# Create your models here.
class Home(models.Model):

    title = models.CharField('Título', max_length=50)
    description = models.TextField()
    contact_email = models.EmailField('Email de contacto', blank=True, null=True)
    web_address = models.CharField('Dirección web', max_length=100, blank=True, null=True)
    image_file_name = models.CharField('Nombre archivo imagen', max_length=50, blank=True, null=True)

    class Meta:

        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página Principal'

    def __str__(self):
        return self.title + '' + self.description + '' + self.contact_email


class SocialMedia(models.Model):
    name_social_network = models.CharField('Nombre red social', max_length=50, blank=True, null=True)
    address_social_network = models.CharField('Dirección red social', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'
    
    def __str__(self):
        return self.name_social_network

