# Generated by Django 2.2.12 on 2020-09-17 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0010_auto_20200916_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='communication_technology_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='station.CommunicationTechnologyStation'),
        ),
    ]
