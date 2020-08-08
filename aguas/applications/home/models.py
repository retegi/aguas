from django.db import models

# Create your models here.
class Home(models.Model):

    title = models.CharField('Título', max_length=50)
    description = models.TextField()
    contact_email = models.EmailField('Email de contacto', blank=True, null=True)

    class Meta:

        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página Principal'

    def __str__(self):
        return self.title + '' + self.description + '' + self.contact_email

