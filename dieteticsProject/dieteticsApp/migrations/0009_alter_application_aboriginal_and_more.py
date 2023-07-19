# Generated by Django 4.2.3 on 2023-07-18 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieteticsApp', '0008_alter_application_aboriginal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='aboriginal',
            field=models.CharField(blank=True, choices=[('True', 'Yes'), ('False', 'No')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='aboriginalChoices',
            field=models.CharField(blank=True, choices=[('First Nations', 'First Nations'), ('Métis', 'Métis'), ('Inuit', 'Inuit')], max_length=100, null=True),
        ),
    ]