from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("<int:id>", views.index, name="home"),
    path("create/", views.create, name="create")
]