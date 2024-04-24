# Generated by Django 4.2.10 on 2024-03-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_rename_mobile_appointments_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='reason',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
