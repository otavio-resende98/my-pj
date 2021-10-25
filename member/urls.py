from django.urls import path

from .views import (
    home,
    new_member,
)

app_name = "member"
urlpatterns = [
     path("", home, name="home"),
     path("member/create/", new_member, name="new_member"),
]
