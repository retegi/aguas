# Generated by Django 2.2.16 on 2020-11-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidence', '0006_auto_20201105_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidence',
            name='repairForecast_incidence',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha previsión reparación'),
        ),
        migrations.DeleteModel(
            name='RepairForecast',
        ),
    ]
