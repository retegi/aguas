# Generated by Django 2.2.16 on 2020-10-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_user_employee'),
        ('preventive', '0034_preventive_employee_preventive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preventive',
            name='employee_preventive',
        ),
        migrations.AddField(
            model_name='preventive',
            name='employee_preventive',
            field=models.ManyToManyField(limit_choices_to={'company': 'Suez Environment'}, related_name='preventives', to='employee.Employee'),
        ),
    ]
