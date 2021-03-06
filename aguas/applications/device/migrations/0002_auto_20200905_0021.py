# Generated by Django 2.2.12 on 2020-09-04 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('url_file', models.CharField(max_length=50, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Archivo dispositivo',
                'verbose_name_plural': 'Archivos de dispositivo',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='typedevice',
            options={'ordering': ['name'], 'verbose_name': 'Tipo dispositivo', 'verbose_name_plural': 'Tipos de dispositivos'},
        ),
        migrations.RemoveField(
            model_name='device',
            name='brand_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='communication_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='image_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='model_device',
        ),
        migrations.RemoveField(
            model_name='device',
            name='type_device',
        ),
        migrations.CreateModel(
            name='ProductModelDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_device', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('model_device', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('communication_device', models.ForeignKey(blank=True, max_length=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.CommunicationDevice')),
                ('file_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.FileDevice')),
                ('image_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.ImageDevice')),
                ('type_device', models.ForeignKey(blank=True, max_length=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.TypeDevice')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['brand_device'],
            },
        ),
        migrations.AddField(
            model_name='device',
            name='product_model_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.ProductModelDevice'),
        ),
    ]
