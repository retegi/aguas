# Generated by Django 3.1.3 on 2020-12-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0006_delete_repairforecast'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='productsToInvoice_repair',
            field=models.TextField(blank=True, null=True, verbose_name='Material a facturar'),
        ),
    ]
