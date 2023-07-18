import datetime
from django.db import models
from django import forms

class Constants(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        ordering = ['name', 'value']

    def __str__(self):
        return self.name
    
# Create your models here.
class Application(models.Model):
    # CWL
    
    # 

    # Form
    # Mandatory fields
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    cei = models.CharField(max_length=100)
    studentNumber = models.IntegerField()
    studentEmail = models.EmailField(max_length=100)
    vertifyStudentEmail = models.CharField(max_length=100)
    preferredEmail = models.EmailField(max_length=100)
    vertifyPreferredEmail = models.EmailField(max_length=100)
    phoneNumber = models.BigIntegerField()
    birthday = models.DateField()
    firstApp = models.CharField(max_length=10, choices=(('True', 'Yes'), ('False', 'No')))
    appTimesDropdown = models.CharField(max_length=2, choices=(
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ("5+", '5+'),
    ))
    # Optional fields
    aboriginal = models.CharField(max_length=10, choices=[('True', 'Yes'), ('False', 'No')])
    aboriginalChoices = models.CharField(max_length=100, choices=[("First Nations", 'First Nations'), ("Métis", 'Métis'), ("Inuit", 'Inuit')])


    def __str__(self):
        return self.name