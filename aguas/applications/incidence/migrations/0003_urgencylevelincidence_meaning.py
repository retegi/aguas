# Generated by Django 2.2.12 on 2020-09-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidence', '0002_auto_20200905_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='urgencylevelincidence',
            name='meaning',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Significado'),
        ),
    ]
