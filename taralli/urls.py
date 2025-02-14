from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("log/weight/", views.log_weight, name="log_weight"),
    path("log/meal/", views.log_meal, name="log_meal"),
    path("data/all/", views.get_logs, name="data_all"),
]
