# Generated by Django 2.2.12 on 2020-09-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0004_auto_20200910_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='video_station',
        ),
        migrations.AddField(
            model_name='station',
            name='video_station',
            field=models.ManyToManyField(blank=True, null=True, to='station.VideoStation'),
        ),
    ]
