# Generated by Django 4.2.3 on 2023-07-17 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieteticsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constants',
            options={'ordering': ['name', 'value']},
        ),
        migrations.RemoveField(
            model_name='constants',
            name='year',
        ),
        migrations.AddField(
            model_name='constants',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constants',
            name='value',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]