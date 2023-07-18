from django.contrib import admin

# Register your models here.
from .models import Constants

# @admin.register(Constants)
class ConstantsAdmin(admin.ModelAdmin):
    fields = ["name", "value"]

admin.site.register(Constants, ConstantsAdmin)

# @admin.register(ApplicationForm)
# class ApplicationFormAdmin(admin.ModelAdmin):
#     fields = ["lastName"]

# admin.site.register(ApplicationForm, ApplicationFormAdmin)