# Generated by Django 2.2.12 on 2020-08-24 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image_imageInstallation', models.ImageField(upload_to='installations/')),
            ],
            options={
                'verbose_name': 'Imagen instalación',
                'verbose_name_plural': 'Imagen de instalaciones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypeInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'TipoInstalación',
                'verbose_name_plural': 'TipoInstalaciones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observations_installation', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('image_installation', models.ManyToManyField(blank=True, null=True, to='installation.ImageInstallation')),
                ('station_installation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.Station')),
                ('type_installation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='installation.TypeInstallation')),
            ],
            options={
                'verbose_name': 'Instalación',
                'verbose_name_plural': 'Instalaciones',
                'ordering': ['station_installation'],
            },
        ),
    ]
