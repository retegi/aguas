# Generated by Django 2.2.16 on 2020-10-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0031_preventive_totalestimatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preventive',
            name='totalEstimatedTime',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tiempo estimado minutos'),
        ),
    ]
