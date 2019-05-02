from django.urls import path

from . import views

app_name = "my_repos"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
