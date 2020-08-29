# Generated by Django 2.2.12 on 2020-08-24 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Area estación')),
                ('color_html_background', models.CharField(blank=True, max_length=7, null=True, verbose_name='Color HTML')),
            ],
            options={
                'verbose_name': 'Area estación',
                'verbose_name_plural': 'Areas de estación',
            },
        ),
        migrations.CreateModel(
            name='ImageStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image_imageStation', models.ImageField(upload_to='stations/')),
            ],
            options={
                'verbose_name': 'Imagen estación',
                'verbose_name_plural': 'Imagen de estaciones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Simulator3DStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Descripción de url')),
                ('url', models.TextField(blank=True, max_length=500, null=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Simulación 3D',
                'verbose_name_plural': 'Simulaciones 3D',
            },
        ),
        migrations.CreateModel(
            name='StatusStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('color_html_background', models.CharField(blank=True, max_length=7, null=True, verbose_name='Color HTML')),
            ],
            options={
                'verbose_name': 'Estado estación',
                'verbose_name_plural': 'Estados de la estación',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypeStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tipo estación')),
                ('acronym', models.CharField(blank=True, max_length=50, null=True, verbose_name='Acrónimo')),
            ],
            options={
                'verbose_name': 'Tipo estación',
                'verbose_name_plural': 'Tipos de estación',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_station', models.CharField(blank=True, max_length=50, null=True, verbose_name='Código')),
                ('name_station', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('latitude_station', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitud')),
                ('longitude_station', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitud')),
                ('observations_station', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('area_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.AreaStation')),
                ('comunication_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comunications_p', to='station.Station')),
                ('image_station', models.ManyToManyField(blank=True, null=True, to='station.ImageStation')),
                ('origin_watertank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origins_wt', to='station.Station')),
                ('simulator3D_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.Simulator3DStation')),
                ('status_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.StatusStation')),
                ('type_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.TypeStation')),
            ],
            options={
                'verbose_name': 'Estación',
                'verbose_name_plural': 'Estaciones',
            },
        ),
    ]
