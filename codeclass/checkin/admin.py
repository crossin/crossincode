from django.contrib import admin

from checkin import models


class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'record', 'exp', 'create_time']


class StatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exp', 'checkin_days', 'running_days',
                    'month_running', 'last_checkin', 'supports']


class SupportAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'supporter', 'support_ip', 'create_time']


admin.site.register(models.Log, LogAdmin)
admin.site.register(models.Stat, StatAdmin)
admin.site.register(models.Support, SupportAdmin)
