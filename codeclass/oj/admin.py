from django import forms
from django.contrib import admin

from oj import models


class QuizForm(forms.ModelForm):
    pre_code = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = models.Quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizForm


admin.site.register(models.Quiz, QuizAdmin)
