# Generated by Django 4.2.5 on 2023-09-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_booking_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='branch',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
