from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
import datetime



def index(request):
    return render(request=request, template_name="index.html")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)