from django.urls import path

from graph import views

app_name = "graph"

urlpatterns = [
    path("", views.graph_view, name="graph_view"),

    path("api/", views.graph_api, name="graph_api"),
]
