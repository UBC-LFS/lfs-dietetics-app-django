from django.db import models
from django import forms

# Create your models here.
class ApplicationForm(forms.Form):
    lastName = forms.CharField(max_length=100, label="Last name")
    firstName = forms.CharField(max_length=100, label="First name")
    cei = forms.CharField(max_length=100, label="Current Educational Institution")
    studentNumber = forms.IntegerField(label="UBC Student Number")
    studentEmail = forms.EmailField(max_length=100, label="UBC Student Email Address")
    vertifyStudentEmail = forms.CharField(max_length=100, label="Verify UBC Student Email Address")
    preferredEmail = forms.EmailField(max_length=100, label="Preferred Email Address")
    vertifyPreferredEmail = forms.EmailField(max_length=100, label="Verify Preferred Email Address")
    phoneNumber = forms.IntegerField(label="Phone Number")
    birthday = forms.DateField(label="Birthday (yyyy-mm-dd)")
    firstApp = forms.ChoiceField(label="Is this your first application to the UBC Dietetics Major?", widget=forms.RadioSelect, choices=[(True, 'Yes'), (False, 'No')])
    appTimesDropdown = forms.NullBooleanField(label="If this is not your first time applying to the program, how many times have you applied in the past?", 
                                              widget=forms.Select(choices=[
                                                    ('0', '0'),
                                                    ('1', '1'),
                                                    ('2', '2'),
                                                    ('3', '3'),
                                                    ('4', '4'),
                                                    ("5+", '5+'),
                                              ]))

    class Meta:
        ordering = ['lastName', 'firstName']

    def __str__(self):
        return self.name
    
