from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def carousel(request):
    return render(request, 'carousel.html')


def test(request):
    return render(request, 'new.html')
