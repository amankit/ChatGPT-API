from django.contrib import admin
from django.urls import path
from chagpt_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatgpt/',views.Chatgpt.as_view()),
]
