from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.

def sign_up_by_html(request):
    users = ['Vlad', 'Oleg', 'Jeka']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif not age.isdigit() or int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        # Возвращаем данные для заполнения полей
        info.update({
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age
        })

        if 'error' in info:
            return render(request, 'fifth_task/registration_page.html',
                          {'info': info})

        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_django(request):
    users = ['Vlad', 'Oleg', 'Jeka']
    info = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            if 'error' in info:
                info.update({
                    'username': username,
                    'password': password,
                    'repeat_password': repeat_password,
                    'age': str(age)
                })
                return render(request, 'fifth_task/registration_page.html',
                              {'form': form, 'info': info})

            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = ContactForm()
    return render(request, 'fifth_task/registration_page.html',
                  {'form': form},)
