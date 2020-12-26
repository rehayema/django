from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rehayema/", views.rehayema, name="rehayema"),
    path("<str:name>", views.greet, name="greet")
]