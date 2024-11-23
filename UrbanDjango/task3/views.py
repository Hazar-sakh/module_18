from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def page1(request):
    return render(request, 'page1.html')


class page2(TemplateView):
    template_name = 'page2.html'
