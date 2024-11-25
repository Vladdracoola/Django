from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fourth_task/main.html')


def games(request):
    game1 = 'World of Warcraft'
    game2 = 'FIFA'
    game3 = 'Heroes of might and magic 3'
    context = {
        'games': [game1, game2, game3]
    }
    return render(request, 'fourth_task/games.html', context)


def books(request):
    book1 = 'Хроники Амбера. Р. Желязны'
    book2 = 'Гарри Поттер. Дж. Роулинг'
    book3 = 'Граф Монте-Кристо. А. Дюма'
    context = {
        'books': [book1, book2, book3]
    }
    return render(request, 'fourth_task/books.html', context)


def menu(request):
    return render(request, template_name='fourth_task/menu.html')
