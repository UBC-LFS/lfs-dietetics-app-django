# Generated by Django 4.2.3 on 2023-07-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieteticsApp', '0012_constant_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constant',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]