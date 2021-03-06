# Generated by Django 2.2.12 on 2020-08-24 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('installation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunicationDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Comunicación del dispositivo',
                'verbose_name_plural': 'Comunicaciones de dispositivos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImageDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image_device', models.ImageField(upload_to='devices/')),
            ],
            options={
                'verbose_name': 'Imagen dispositivo',
                'verbose_name_plural': 'Imagen de dispositivos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypeDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo dispositivo',
                'verbose_name_plural': 'Tipo de dispositivos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_device', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('model_device', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('serial_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='NºSerie')),
                ('ip_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='IP')),
                ('pin_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='PIN')),
                ('puk_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='PUK')),
                ('slave_num_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nº Esclavo')),
                ('tel_long_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tel LARGO')),
                ('tel_short_device', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tel CORTO')),
                ('observations_device', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('communication_device', models.ForeignKey(blank=True, max_length=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.CommunicationDevice')),
                ('image_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.ImageDevice')),
                ('installation_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='installation.Installation')),
                ('parent_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
                ('type_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.TypeDevice')),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
                'ordering': ['installation_device'],
            },
        ),
    ]
