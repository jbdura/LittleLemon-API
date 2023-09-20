# Generated by Django 4.2.5 on 2023-09-20 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]