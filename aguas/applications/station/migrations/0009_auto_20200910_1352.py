# Generated by Django 2.2.12 on 2020-09-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0008_auto_20200910_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docstation',
            name='url_docStation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Url'),
        ),
    ]