# Generated by Django 2.2.16 on 2020-10-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0013_auto_20201001_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='preventive',
            name='autLithiumBatteryStatus_preventiveDetail_preventive',
            field=models.TextField(blank=True, max_length=40, null=True, verbose_name='Observaciones estado de baterías'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autLithiumBatteryStatus_preventive',
            field=models.CharField(blank=True, choices=[('1', 'OK'), ('2', 'No OK'), ('3', 'NP')], max_length=40, null=True, verbose_name='Estado de batería de litio'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autVisualInspectionOfAlarmLedStatus_preventive',
            field=models.CharField(choices=[('1', 'OK'), ('2', 'No OK'), ('3', 'NP')], default='1', max_length=20, verbose_name='Estado de LEDs de alarma'),
        ),
    ]
