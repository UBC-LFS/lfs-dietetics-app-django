from django.contrib import admin
from .models import Constant, Application
from django.utils.safestring import mark_safe

class ConstantsAdmin(admin.ModelAdmin):
    fields = ["name", "value", "helpText"]
    list_display = ('name', 'value', 'helpText')

class ApplicantsAdmin(admin.ModelAdmin):
    fields = ["cwl", "applicationNumber", "dateApplied", "lastName", "firstName", "cei", "studentNumber", "studentEmail", "vertifyStudentEmail", "preferredEmail", "vertifyPreferredEmail", "phoneNumber", "birthday", "firstApp", "appTimesDropdown", "aboriginal", "aboriginalChoices"]
    list_display = ('applicationNumber', 'firstName' , 'lastName', 'cwl', 'studentNumber', 'dateApplied')
    list_filter = ('appTimesDropdown', 'aboriginal', 'aboriginalChoices')

admin.site.register(Application, ApplicantsAdmin)
admin.site.register(Constant, ConstantsAdmin)
