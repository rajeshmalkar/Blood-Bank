# Generated by Django 4.2.10 on 2024-03-09 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_appointments_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='mobile',
            new_name='phone',
        ),
    ]
