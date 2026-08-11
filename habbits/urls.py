from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("add/", views.add_habbit, name = "add_habbit"),
    path("update/<int:id>/", views.update_habbit, name="update_habbit"),
    path("delete/<int:id>/", views.delete_habbit, name="delete_habbit"),
    path("complete/<int:id>/", views.complete_today, name="complete_today"),  
] 