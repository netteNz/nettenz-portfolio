from django.contrib import admin
from django.urls import path, include
from blog.views import BlogView, ContentView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view()),
    path('content/', ContentView.as_view())
]
