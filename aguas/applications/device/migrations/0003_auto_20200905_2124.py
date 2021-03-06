# Generated by Django 2.2.12 on 2020-09-05 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_auto_20200905_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='productmodeldevice',
            name='brand_device',
            field=models.ForeignKey(blank=True, max_length=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.BrandDevice'),
        ),
    ]
