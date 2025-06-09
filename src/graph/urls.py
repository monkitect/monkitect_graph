from django.urls import path

from graph import views

app_name = "graph"

urlpatterns = [
    path('', views.index, name='index'),
]
