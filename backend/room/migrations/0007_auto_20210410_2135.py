# Generated by Django 3.1.7 on 2021-04-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_auto_20210410_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='status',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_no',
            field=models.IntegerField(unique=True),
        ),
    ]
