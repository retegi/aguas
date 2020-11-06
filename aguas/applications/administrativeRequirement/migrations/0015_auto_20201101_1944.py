# Generated by Django 2.2.16 on 2020-11-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativeRequirement', '0014_auto_20201101_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anomaly', models.CharField(blank=True, max_length=50, null=True, verbose_name='Anomalía')),
                ('color_anomaly', models.CharField(blank=True, max_length=12, null=True, verbose_name='Color anomalía')),
            ],
            options={
                'verbose_name': 'Anomalía',
                'verbose_name_plural': 'Anomalías',
                'ordering': ['anomaly'],
            },
        ),
        migrations.AlterField(
            model_name='status',
            name='color_status',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Color situación'),
        ),
        migrations.AddField(
            model_name='administrativerequirement',
            name='anomaly_AR',
            field=models.ManyToManyField(to='administrativeRequirement.Anomaly'),
        ),
    ]
