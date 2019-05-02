from django.urls import path

from . import views

app_name = "starred_gists"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
