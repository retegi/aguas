# Generated by Django 2.2.16 on 2020-11-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetMap', '0005_address_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='detail_contact',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Detalles del contacto'),
        ),
        migrations.RemoveField(
            model_name='address',
            name='contact_Address',
        ),
        migrations.AddField(
            model_name='address',
            name='contact_Address',
            field=models.ManyToManyField(to='streetMap.Contact'),
        ),
    ]