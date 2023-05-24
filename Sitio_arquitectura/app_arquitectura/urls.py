from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("courses", views.courses, name="courses"),
    path("about_us", views.about_us, name="about_us"),
]