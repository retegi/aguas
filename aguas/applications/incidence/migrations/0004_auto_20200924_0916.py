# Generated by Django 2.2.16 on 2020-09-24 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidence', '0003_urgencylevelincidence_meaning'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urgencylevelincidence',
            options={'ordering': ['-id'], 'verbose_name': 'Nivel de urgencia', 'verbose_name_plural': 'Niveles de urgencia'},
        ),
    ]
