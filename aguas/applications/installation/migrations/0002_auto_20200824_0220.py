# Generated by Django 2.2.12 on 2020-08-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='image_installation',
            field=models.ManyToManyField(blank=True, to='installation.ImageInstallation'),
        ),
    ]