# Generated by Django 2.2.12 on 2020-08-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('description', models.TextField()),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email de contacto')),
                ('web_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección web')),
                ('image_file_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre archivo imagen')),
            ],
            options={
                'verbose_name': 'Página Principal',
                'verbose_name_plural': 'Página Principal',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_social_network', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre red social')),
                ('address_social_network', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección red social')),
            ],
            options={
                'verbose_name': 'Red social',
                'verbose_name_plural': 'Redes sociales',
            },
        ),
    ]