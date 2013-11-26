from django.template.response import HttpResponse


def index_view(request):
    return HttpResponse("Welcome to Crossin Code Class!")
