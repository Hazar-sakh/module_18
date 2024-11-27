from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30,
                               label='Логин',
                               required=True,
                               initial='Введите логин')
    password = forms.CharField(min_length=8,
                               label='Пароль',
                               required=True,
                               initial='Введите пароль')
    repeat_password = forms.CharField(min_length=8,
                                      label='Подтвердите пароль',
                                      required=True,
                                      initial='Подтвердите пароль')
    age = forms.CharField(max_length=3,
                          label='Ваш возраст',
                          required=True,
                          initial='Введите возраст')
