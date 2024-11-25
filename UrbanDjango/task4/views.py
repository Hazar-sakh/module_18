from django.shortcuts import render

# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def main_page(request):
    return render(request, 'main_page.html')


def page1(request):
    first = 'Манчжур'
    second = 'Черные пантеры'
    third = 'Тайфун'
    context1 = {
        'first': first,
        'second': second,
        'third': third
    }
    return render(request, 'page1.html', context1)


def page2(request):
    list_of_referees = ['Дроздов А. - 1 категория', 'Болотова С. - 2 категория',
                        'Лаврентьев Е. - 3 категория']
    context2 = {'list_of_referees': list_of_referees}
    return render(request, 'page2.html', context2)
