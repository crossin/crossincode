from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from checkin import models


def home(request):
    if request.user.is_authenticated():
        return redirect(checkin)
    return TemplateResponse(request, 'checkin/index.html', {})


def success(request, test='123'):
    print request
    print test
    return TemplateResponse(request, 'checkin/success.html', {})


def checkin(request):
    if not request.user.is_authenticated():
        return redirect(home)
    if request.method == 'POST':
        record = request.POST.get('record')
        models.Log.objects.create(user=request.user, record=record)
#        return redirect(success, test='456')
        return HttpResponseRedirect(reverse('checkin-success', kwargs={'test': 456}))
    return TemplateResponse(request, 'checkin/checkin.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(checkin)
    return TemplateResponse(request, 'checkin/login.html', {})


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect(checkin)
    return TemplateResponse(request, 'checkin/register.html', {})
