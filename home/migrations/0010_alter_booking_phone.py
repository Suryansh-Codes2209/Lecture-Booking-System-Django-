# Generated by Django 4.2.5 on 2023-09-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_booking_branch_alter_booking_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=12),
        ),
    ]
