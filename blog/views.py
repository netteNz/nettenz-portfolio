from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name="index.html"

class ContentView(TemplateView):
    template_name="content.html"
