from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def page1(request):
    return render(request, 'page1.html')


def page2(request):
    list_of_referees = ['Дроздов А. - 1 категория', 'Болотова С. - 2 категория',
                        'Лаврентьев Е. - 3 категория']
    context = {'list_of_referees': list_of_referees}
    return render(request, 'page2.html', context)
