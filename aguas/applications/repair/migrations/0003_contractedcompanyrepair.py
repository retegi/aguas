# Generated by Django 2.2.16 on 2020-10-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_statusafterrepair_color_html_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractedCompanyRepair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contractedCompanyRepair', models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre empresa contratada Mant Correctivo')),
            ],
            options={
                'verbose_name': 'Empresa contratada mantenimiento correctivo',
                'verbose_name_plural': 'Empresas contratadas mantenimiento correctivo',
                'ordering': ['name_contractedCompanyRepair'],
            },
        ),
    ]
