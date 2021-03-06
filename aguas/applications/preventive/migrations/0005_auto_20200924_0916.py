# Generated by Django 2.2.16 on 2020-09-24 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0004_auto_20200922_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_partName', models.CharField(max_length=30, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Nombre de parte de revisión',
                'verbose_name_plural': 'Nombres de partes de revisión',
                'ordering': ['name_partName'],
            },
        ),
        migrations.RenameField(
            model_name='partpreventive',
            old_name='station_partPreventive',
            new_name='preventive_partPreventive',
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='partName_parPreventive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preventive.PartName'),
        ),
    ]
