# Generated by Django 2.2.12 on 2020-09-14 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20200905_2124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileDevice',
            new_name='DocDevice',
        ),
        migrations.AlterModelOptions(
            name='docdevice',
            options={'ordering': ['name_docDevice'], 'verbose_name': 'Archivo dispositivo', 'verbose_name_plural': 'Archivos de dispositivo'},
        ),
        migrations.RenameField(
            model_name='docdevice',
            old_name='name',
            new_name='name_docDevice',
        ),
        migrations.RenameField(
            model_name='docdevice',
            old_name='url_file',
            new_name='url_docDevice',
        ),
        migrations.RenameField(
            model_name='productmodeldevice',
            old_name='file_device',
            new_name='doc_device',
        ),
    ]
