from django.urls import path
from users import views
# from django.contrib.auth import views as auth_views
# from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]