from django.views.generic.base import TemplateView
from django.http import HttpResponse

# index = TemplateView.as_view(template_name='index.html')

def index(request):
    return HttpResponse("it's for backend page")
