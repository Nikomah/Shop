from django.shortcuts import render


def index(request):
    data = {
        'message': 'hello!!!'
    }
    return render(request, 'index.html', context=data)
