from django.urls import path, include
from . import views


urlpatterns = [
        path("", views.blog_index, name="blog_index"),

]