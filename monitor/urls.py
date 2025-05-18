from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashboard, name="dash"),
    path("api/stats/", views.stats_api),
]
