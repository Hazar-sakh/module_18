from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def index1(request):
    return render(request, 'index1.html')


class index2(TemplateView):
    template_name = 'index2.html'


