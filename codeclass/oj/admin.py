from django import forms
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from oj import models


class QuizForm(forms.ModelForm):
    pre_code = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = models.Quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizForm


class SampleForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, required=False)
    code = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = models.Sample


class SampleResource(resources.ModelResource):
    class Meta:
        model = models.Sample


class SampleAdmin(ImportExportModelAdmin):
    resource_class = SampleResource
    form = SampleForm
    list_display = ['id', 'seq', 'title']


admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Sample, SampleAdmin)
