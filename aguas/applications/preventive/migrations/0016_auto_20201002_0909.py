# Generated by Django 2.2.16 on 2020-10-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0015_auto_20201002_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preventive',
            name='autLithiumBatteryStatusNoOkDetail_preventive',
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autHardwareDiagnosisNoOkDetail_preventive',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Observaciones diagnóstico de Hardware'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autHardwareDiagnosis_preventive',
            field=models.CharField(blank=True, choices=[('1', 'OK'), ('2', 'No OK'), ('3', 'NP')], default='1', max_length=40, null=True, verbose_name='Diagnóstico de Hardware'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autLithiumBatteryStatus_preventive',
            field=models.CharField(blank=True, choices=[('1', 'OK'), ('2', 'No OK'), ('3', 'NP')], default='1', max_length=40, null=True, verbose_name='Estado de batería de litio'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autVisualInspectionOfAlarmLedStatusNoOkDetail_preventive',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Observaciones estado de LEDs de alarma'),
        ),
    ]