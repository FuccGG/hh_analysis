from django.shortcuts import render
from django.shortcuts import render
from .apidata import get_api_data


def index(request):
    apidata = get_api_data()
    return render(request, 'index.html', {'apidata': apidata})

