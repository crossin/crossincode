from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from runcode import run


def wechat_view(request):
    return TemplateResponse(request, 'oj/wechat.html', {})


def output_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        result = run(code, '')
        return TemplateResponse(
            request,
            'oj/output.html',
            {
                'code': code,
                'result': result[0],
            })
    return HttpResponseRedirect(reverse(wechat_view))
