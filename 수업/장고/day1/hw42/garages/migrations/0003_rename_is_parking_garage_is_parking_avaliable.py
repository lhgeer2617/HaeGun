# Generated by Django 4.2.5 on 2023-09-15 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0002_alter_garage_closing_time_alter_garage_opening_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garage',
            old_name='is_parking',
            new_name='is_parking_avaliable',
        ),
    ]
