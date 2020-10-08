# Generated by Django 2.2.16 on 2020-10-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0025_auto_20201002_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='preventive',
            name='saistatusOfConnectorsAndLEDsNoOkDetail_preventive',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Observaciones estado de conectores y Leds'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='saistatusOfConnectorsAndLEDs_preventive',
            field=models.CharField(blank=True, choices=[('1', 'OK'), ('2', 'No OK'), ('3', 'NP')], default='1', max_length=40, null=True, verbose_name='Estado de conectores y Leds'),
        ),
    ]