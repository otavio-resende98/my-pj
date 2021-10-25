from django.urls import path

from .views import (
    new_activity,
)

app_name = "Atividade"
urlpatterns = [
     path("create/", new_activity, name="new_activity"),
]
