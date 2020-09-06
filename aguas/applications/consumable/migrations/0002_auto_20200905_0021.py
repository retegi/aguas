# Generated by Django 2.2.12 on 2020-09-04 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeconsumable',
            options={'ordering': ['name'], 'verbose_name': 'Tipo consumible', 'verbose_name_plural': 'Tipos de consumibles'},
        ),
        migrations.RemoveField(
            model_name='consumable',
            name='type_consumable',
        ),
        migrations.RemoveField(
            model_name='typeconsumable',
            name='brand_typeConsumable',
        ),
        migrations.RemoveField(
            model_name='typeconsumable',
            name='imagen_typeConsumable',
        ),
        migrations.RemoveField(
            model_name='typeconsumable',
            name='model_typeConsumable',
        ),
        migrations.RemoveField(
            model_name='typeconsumable',
            name='observations_typeConsumable',
        ),
        migrations.RemoveField(
            model_name='typeconsumable',
            name='type_typeConsumable',
        ),
        migrations.RemoveField(
            model_name='typeconsumable',
            name='voltage_ouput_typeConsumable',
        ),
        migrations.AddField(
            model_name='typeconsumable',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.CreateModel(
            name='TypeModelConsumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_typeConsumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('model_typeConsumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('voltage_ouput_typeConsumable', models.CharField(choices=[('0', '7.2V'), ('1', '3.6V')], max_length=1, null=True, verbose_name='SalidaVoltaje')),
                ('observations_typeConsumable', models.CharField(blank=True, max_length=50, null=True, verbose_name='Observaciones')),
                ('imagen_typeConsumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumable.ImageConsumable')),
                ('type_consumable_typeConsumable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumable.TypeConsumable')),
            ],
        ),
        migrations.AddField(
            model_name='consumable',
            name='type_model_consumable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consumable.TypeModelConsumable'),
        ),
    ]
