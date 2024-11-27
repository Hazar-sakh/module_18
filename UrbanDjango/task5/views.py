from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.


def sign_up_by_html(request):
    users = ['Masha', 'Grisha', 'Sasha', 'Pasha']
    info = {}
    context = {
        'info': info
    }
    user = None
    context2 = {
        'uZr': user
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают!'})
            return render(request, 'registration_page.html', context)
        elif age < 18:
            info.update({'error': 'Вы должны быть старше 18!'})
            return render(request, 'registration_page.html', context)
        elif username in users:
            info.update({'error': 'Пользователь уже существует!'})
            return render(request, 'registration_page.html', context)
        elif password == repeat_password and age >= 18:
            context2.update({'uZr': f'Приветствуем, {username}!'})
            return render(request, 'registration_page.html', context2)
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    users = ['Masha', 'Grisha', 'Sasha', 'Pasha']
    info = {}
    context = {
        'info': info
    }
    user = None
    context2 = {
        'uZr': user
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if password != repeat_password:
                info.update({'error': 'Пароли не совпадают!'})
                return render(request, 'registration_page.html', context)
            elif age < 18:
                info.update({'error': 'Вы должны быть старше 18!'})
                return render(request, 'registration_page.html', context)
            elif username in users:
                info.update({'error': 'Пользователь уже существует!'})
                return render(request, 'registration_page.html', context)
            elif password == repeat_password and age >= 18:
                context2.update({'uZr': f'Приветствуем, {username}!'})
                return render(request, 'registration_page.html', context2)
    return render(request, 'registration_page.html')

