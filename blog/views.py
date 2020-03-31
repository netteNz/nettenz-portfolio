from django.shortcuts import render
from django.http import HttpResponse


def blog_index(request):
    return render(request, 'index.html', {})