from django.contrib import admin

from member import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exp', 'gold']


admin.site.register(models.Student, StudentAdmin)
