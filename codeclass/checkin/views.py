from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
