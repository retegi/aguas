# Generated by Django 2.2.16 on 2020-10-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0012_auto_20200927_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='preventive',
            name='autVisualInspectionOfAlarmLedStatusNoOkDetail_preventive',
            field=models.TextField(blank=True, max_length=40, null=True, verbose_name='Observaciones o fallo en estado alarmas de Led'),
        ),
        migrations.AlterField(
            model_name='preventive',
            name='autVisualInspectionOfAlarmLedStatus_preventive',
            field=models.CharField(choices=[('1', 'OK'), ('2', 'No OK'), ('3', 'NP')], default='1', max_length=20),
        ),
    ]