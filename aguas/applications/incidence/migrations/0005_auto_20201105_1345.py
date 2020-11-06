# Generated by Django 2.2.16 on 2020-11-05 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidence', '0004_auto_20200924_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_RF', models.DateTimeField(blank=True, null=True, verbose_name='Fecha prevista reparación')),
            ],
            options={
                'verbose_name': 'Fecha prevista reparación',
                'verbose_name_plural': 'Fecha prevista reparaciones',
                'ordering': ['date_RF'],
            },
        ),
        migrations.AddField(
            model_name='incidence',
            name='repairForecast_incidence',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='incidence.RepairForecast'),
        ),
    ]
