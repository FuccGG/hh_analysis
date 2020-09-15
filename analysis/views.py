from django.shortcuts import render
from django.shortcuts import render
from . apidata2 import get_api_data


def index(request):
    apidata = get_api_data()
    return render(request, 'index.html', {'apidata': apidata[0], 'frequencies': apidata[1]})

