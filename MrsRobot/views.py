from django.http import HttpResponse
from django.shortcuts import render
from . import app


def whoami(request):
    return render(request, 'whoami.html')


def ability(request):
    return render(request, 'ability.html')


def speaking(request):
    return render(request, 'speaking.html')


def index(request):
    html = ''
    if request.method == 'POST':
        query = request.POST['query']
        answer = app.process_query(query)
        html = f'<mark>{answer}</mark>'
    context = {
        'response': html,
        'where': request.path
    }

    return render(request, 'index.html', context)
