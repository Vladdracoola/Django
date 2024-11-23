from django.shortcuts import render


# Create your views here.
def index(request):
    title = 'Мой сайт'

    context = {
        'title': title
    }
    return render(request, 'third_task/main.html', context)

def games(request):
    title = 'Мои любимые игры'
    game1 = 'World of Warcraft'
    game2 = 'FIFA'
    game3 = 'Heroes of might and magic 3'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3
    }
    return render(request, 'third_task/games.html', context)

def books(request):
    title = 'Мои любимые книги'
    book1 = 'Хроники Амбера. Р. Желязны'
    book2 = 'Гарри Поттер. Дж. Роулинг'
    book3 = 'Граф Монте-Кристо. А. Дюма'
    context = {
        'title': title,
        'book1': book1,
        'book2': book2,
        'book3': book3
    }
    return render(request, 'third_task/books.html', context)