# Generated by Django 2.2.16 on 2020-11-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativeRequirement', '0009_administrativerequirement_address_ar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativerequirement',
            name='address_AR',
            field=models.ManyToManyField(to='streetMap.Address'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
