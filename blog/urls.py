from django.urls import path, include
from . import views, BlogView, ContentView


urlpatterns = [
        path("index/", BlogView.as_view()),
        path("content/", views.content)
]
