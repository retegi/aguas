# Generated by Django 2.2.12 on 2020-09-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0002_auto_20200905_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationtechnologystation',
            name='acronym',
            field=models.CharField(max_length=40, verbose_name='Significado'),
        ),
        migrations.AlterField(
            model_name='communicationtechnologystation',
            name='url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL'),
        ),
    ]
