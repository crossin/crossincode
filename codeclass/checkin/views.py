from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse


def home(request):
    if request.user.is_authenticated():
        return redirect(checkin)
    return TemplateResponse(request, 'checkin/index.html', {})


def checkin(request):
    if not request.user.is_authenticated():
        return redirect(home)
    return TemplateResponse(request, 'checkin/checkin.html', {})


def login(request):
    if request.method == 'POST':
        return redirect(checkin)
    return TemplateResponse(request, 'checkin/login.html', {})


def register(request):
    return TemplateResponse(request, 'checkin/register.html', {})
