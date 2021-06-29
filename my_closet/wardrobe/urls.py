from django.urls import path    

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("form", views.form, name="form")
]