# Generated by Django 4.2.5 on 2023-09-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
