from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from runcode import run
from . import models


def wechat_view(request):
    code = request.POST.get('code', '')
    url = request.POST.get('url', '')
    return TemplateResponse(
        request,
        'oj/wechat.html',
        {
            'code': code,
            'url': url,
        })


def output_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        result = run(code, '')
        url = request.POST.get('url', '')
        return TemplateResponse(
            request,
            'oj/output.html',
            {
                'code': code,
                'result': result[0],
                'url': url,
            })
    return HttpResponseRedirect(reverse(wechat_view))


def sample_list(request):
    samples = models.Sample.objects.all()
    return TemplateResponse(
        request,
        'oj/sample_list.html',
        {
            'samples': samples,
        })


def sample_view(request, sample_id):
    sample = models.Sample.objects.get(id=sample_id)
    return TemplateResponse(
        request,
        'oj/sample.html',
        {
            'sample': sample,
        })
