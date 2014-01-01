from django.template.response import TemplateResponse

def index_view(request):
#    languages = models.Language.objects.all()
    return TemplateResponse(request, 'wechat/index.html', {})
