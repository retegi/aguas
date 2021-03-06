# Generated by Django 2.2.16 on 2020-11-01 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streetMap', '0004_auto_20201101_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre')),
                ('lastname_contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='Apellido')),
                ('phone1_contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono1')),
                ('phone2_contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono2')),
                ('email_contact', models.EmailField(blank=True, max_length=40, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['lastname_contact'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_Address', models.CharField(max_length=20, verbose_name='Número calle')),
                ('contact_Address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='streetMap.Contact')),
                ('street_Address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='streetMap.StreetMap')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
                'ordering': ['number_Address'],
            },
        ),
    ]
