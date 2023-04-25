# Generated by Django 4.2 on 2023-04-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workhours',
            options={'ordering': ['date', 'start_time']},
        ),
        migrations.AlterField(
            model_name='organization',
            name='end_time',
            field=models.TimeField(verbose_name='Время оканчания работы'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='stat_time',
            field=models.TimeField(verbose_name='Время начинание работы'),
        ),
    ]
