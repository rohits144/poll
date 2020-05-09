from django.urls import path

from .views import CreatePoll, index

urlpatterns = [
    path("", index, name="index"),
    path("create/", CreatePoll.as_view(), name="create"),

]