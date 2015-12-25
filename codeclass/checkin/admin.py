from django.contrib import admin

from checkin import models


class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'record', 'create_time']


class StatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exp', 'checkin_days', 'running_days', 'month_running',
                    'last_checkin']


admin.site.register(models.Log, LogAdmin)
admin.site.register(models.Stat, StatAdmin)
