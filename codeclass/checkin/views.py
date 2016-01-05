import datetime
from itertools import chain
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


def check_support(user_id, request_user, ip):
    recent = datetime.datetime.now() - datetime.timedelta(hours=1)
    if request_user.is_authenticated():
        supporter = request_user
        done = models.Support.objects.filter(
            user=user_id,
            supporter=supporter,
            create_time__gt=recent
        )
    else:
        supporter = None
        done = models.Support.objects.filter(
            user=user_id,
            supporter=supporter,
            support_ip=ip,
            create_time__gt=recent
        )
    return done, supporter


def success(request):
    user_id = request.GET.get('user')
    owner = User.objects.get(id=user_id)
    stat = owner.stat
    if owner == request.user:
        return TemplateResponse(request, 'checkin/success.html',
                                {'stat': stat})
    else:
        last_log = owner.log_set.order_by('-id')[0]
        ip = request.META.get('REMOTE_ADDR', '')
        done, s = check_support(user_id, request.user, ip)
        return TemplateResponse(request, 'checkin/share.html', {
            'stat': stat,
            'last_log': last_log,
            'done': done
        })


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
    user_others = models.Stat.objects.exclude(user=owner).order_by('-exp')
    user_list_1 = user_others.filter(exp__gt=stat.exp)[:5]
    user_list_2 = user_others.filter(
        exp__lte=stat.exp)[:10-user_list_1.count()]
    return TemplateResponse(request, 'checkin/profile.html', {
        'stat': stat,
        'log_list': log_list,
        'user_list': chain(user_list_1, user_list_2)
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
        return HttpResponseRedirect('/checkin/success/?user=%d' % user.id)
    return TemplateResponse(request, 'checkin/checkin.html', {})


def support(request):
    ip = request.META.get('REMOTE_ADDR', '')
    user_id = request.GET.get('user')
    done, supporter = check_support(user_id, request.user, ip)
    if not done:
        stat = models.Stat.objects.get(user_id=user_id)
        stat.supports += 1
        stat.save()
        models.Support.objects.create(
            user=stat.user,
            supporter=supporter,
            support_ip=ip
        )
    return HttpResponseRedirect('/checkin/success?user=%s' % user_id)


def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(checkin)
        else:
            error = 'login error'
    return TemplateResponse(request, 'checkin/login.html', {'error': error})


def register_user(request):
    error = ''
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
        else:
            error = 'register error'
    return TemplateResponse(request, 'checkin/register.html', {'error': error})
