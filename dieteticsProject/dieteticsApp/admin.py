from django.contrib import admin
from .models import Constants, Application
from django.utils.safestring import mark_safe

class ConstantsAdmin(admin.ModelAdmin):
    fields = ["name", "value"]

class ApplicantsAdmin(admin.ModelAdmin):
        fields = ["cwl", "applicationNumber", "dateApplied", "lastName", "firstName", "cei", "studentNumber", "studentEmail", "vertifyStudentEmail", "preferredEmail", "vertifyPreferredEmail", "phoneNumber", "birthday", "firstApp", "appTimesDropdown", "aboriginal", "aboriginalChoices"]

admin.site.register(Application, ApplicantsAdmin)
admin.site.register(Constants, ConstantsAdmin)
