from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("contact", views.contact, name="contact"),
    path("courses", views.courses, name="courses"),
    path("about_us", views.about_us, name="about_us"),
]