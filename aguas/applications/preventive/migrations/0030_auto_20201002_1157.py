# Generated by Django 2.2.16 on 2020-10-02 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventive', '0029_auto_20201002_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preventive',
            options={'ordering': ['id'], 'verbose_name': 'Mant Preventivo', 'verbose_name_plural': 'Mant Preventivos'},
        ),
        migrations.RemoveField(
            model_name='preventive',
            name='code_preventive',
        ),
    ]