from django import forms
from .models import Application
from django.utils.safestring import mark_safe

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["lastName", "firstName", "cei", "studentNumber", "studentEmail", "vertifyStudentEmail", "preferredEmail", "vertifyPreferredEmail", "phoneNumber", "birthday", "firstApp", "appTimesDropdown", "aboriginal", "aboriginalChoices"]
        labels = {
            "lastName": "Last name",
            "firstName": "First name",
            "cei": "Current Educational Institution",
            "studentNumber": "UBC Student Number",
            "studentEmail": mark_safe('UBC Student Email Address (sign up <a href="https://www.myaccount.ubc.ca/myAccount/" target="_blank" rel="noopener noreferrer">here</a>)'),
            "vertifyStudentEmail": "Verify UBC Student Email Address",
            "preferredEmail": "Preferred Email Address",
            "vertifyPreferredEmail": "Verify Preferred Email Address",
            "phoneNumber": "Phone Number",
            "birthday": "Birthday (yyyy-mm-dd)",
            "firstApp": "Is this your first application to the UBC Dietetics Major?",
            "appTimesDropdown": "If this is not your first time applying to the program, how many times have you applied in the past?",
            "aboriginal": "Do you identify yourself as an Aboriginal person of Canada?",
            "aboriginalChoices": "Do you identify with one or more of the following?"
        }


