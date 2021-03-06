# Generated by Django 2.2.16 on 2020-09-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0007_auto_20200924_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='partpreventive',
            name='autDIandAIinCCStatus',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ED y EA que puedan estar dudosas en CC'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='autHardwareDiagnosis',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Diagnóstico de Hardware'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='autLithiumBatteryStatus',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Estado de batería de litio'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='autVisualInspectionOfAlarmLedStatus',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Inspección estado alarmas de Led'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='autcheckRxTxOnCommunicationCards',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Comprobar Rx yTx en tarjetas de comunicaciones'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='gencleaningVentilationFilters',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Limpieza de filtros de ventilación'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='genelementCleaning',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Limpieza de elementos'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='genfreeOfCorrosion',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Libre de corrosión'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='genupdatedSignalList',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Lista de señales actualizada'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='genventilationSystemAndThermostat',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Sistema de ventilación y termostato'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='saibatteryStatus',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Estado de las baterías'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='saicleaning',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Limpieza, si procede'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='saiinputVoltageMeasurement',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Medida de tensión de entrada'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='saioutputVoltageToConsumption',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Comprobar tensión de salida a consumo'),
        ),
        migrations.AddField(
            model_name='partpreventive',
            name='saistatusOfConnectorsAndLEDs',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Estado de conectores y Leds'),
        ),
    ]
