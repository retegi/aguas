# Generated by Django 2.2.16 on 2020-09-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0011_contractedcompanypreventive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractedcompanypreventive',
            name='name_contractedCompanyPrevent',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre empresa contratada Mant Preventivo'),
        ),
    ]
