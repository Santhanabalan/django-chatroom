# Generated by Django 4.1 on 2022-09-20 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_partcicipants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='partcicipants',
            new_name='participants',
        ),
    ]