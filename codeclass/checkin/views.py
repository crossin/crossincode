import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from checkin import models


def home(request):
    if request.user.is_authenticated():
        return redirect(checkin)
    return TemplateResponse(request, 'checkin/index.html', {})


def success(request):
    stat = request.user.stat
    return TemplateResponse(request, 'checkin/success.html', {'stat': stat})


def profile(request):
    user_id = request.GET.get('user')
    if user_id:
        owner = User.objects.get(id=user_id)
    else:
        if not request.user.is_authenticated():
            return redirect(home)
        owner = request.user
    stat = owner.stat
    log_list = models.Log.objects.filter(user=owner).order_by('-id')
    user_list = models.Stat.objects.exclude(user=owner).order_by('-exp')[:10]
    return TemplateResponse(request, 'checkin/profile.html', {
        'stat': stat,
        'log_list': log_list,
        'user_list': user_list
    })


exp_days = (1, 2, 2, 3, 3, 3, 4)


def checkin(request):
    user = request.user
    if not user.is_authenticated():
        return redirect(home)
    if request.method == 'POST':
        record = request.POST.get('record')
        # add stat
        stat = user.stat
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        exp = 0
        if stat.last_checkin <= yesterday:
            if stat.last_checkin < yesterday:
                stat.running_days = 0
            exp = exp_days[min(stat.running_days, 6)]
            stat.exp += exp
            stat.checkin_days += 1
            stat.running_days += 1
            stat.month_running += 1
            stat.last_checkin = today
            stat.save()
        models.Log.objects.create(user=user, record=record, exp=exp)
        return HttpResponseRedirect('/checkin/success?user=%d' % user.id)
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
            models.Stat.objects.create(user=user)
            login(request, user)
            return redirect(checkin)
    return TemplateResponse(request, 'checkin/register.html', {})
