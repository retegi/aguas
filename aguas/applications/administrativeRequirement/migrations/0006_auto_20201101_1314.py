# Generated by Django 2.2.16 on 2020-11-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativeRequirement', '0005_auto_20201101_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativerequirement',
            name='file_AR',
            field=models.FileField(upload_to='media/administrativeRequirement/'),
        ),
    ]
