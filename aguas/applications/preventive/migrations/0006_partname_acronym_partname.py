# Generated by Django 2.2.16 on 2020-09-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0005_auto_20200924_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='partname',
            name='acronym_partName',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='acrónimo'),
        ),
    ]
