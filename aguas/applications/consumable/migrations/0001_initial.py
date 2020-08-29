# Generated by Django 2.2.12 on 2020-08-24 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageConsumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_imageConsumable', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image_imageConsumable', models.ImageField(upload_to='consumibles/')),
            ],
            options={
                'verbose_name': 'Imagen consumible',
                'verbose_name_plural': 'Imagen de consumibles',
                'ordering': ['name_imageConsumable'],
            },
        ),
        migrations.CreateModel(
            name='StatusConsumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('color_html_background', models.CharField(blank=True, max_length=7, null=True, verbose_name='Color HTML incluir #')),
            ],
            options={
                'verbose_name': 'Estado consumible',
                'verbose_name_plural': 'Estados del consumible',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypeConsumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_typeConsumable', models.CharField(choices=[('0', 'Batería'), ('1', 'Otro')], max_length=1, null=True, verbose_name='TipoConsumible')),
                ('brand_typeConsumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('model_typeConsumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('voltage_ouput_typeConsumable', models.CharField(choices=[('0', '7.2V'), ('1', '3.6V')], max_length=1, null=True, verbose_name='SalidaVoltaje')),
                ('observations_typeConsumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Observaciones')),
                ('imagen_typeConsumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumable.ImageConsumable')),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_placemente_consumable', models.DateTimeField(blank=True, null=True, verbose_name='FechaColocacion')),
                ('serial_num_consumable', models.CharField(blank=True, max_length=100, null=True, verbose_name='NºSerie')),
                ('observations_consumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Observaciones')),
                ('parent_device_consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
                ('status_consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumable.StatusConsumable')),
                ('type_consumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumable.TypeConsumable')),
            ],
        ),
    ]