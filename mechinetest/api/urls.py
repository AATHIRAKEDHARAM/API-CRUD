from django.urls import re_path as url
from django.urls import path
from.import views


urlpatterns = [
    url(r"^create$", views.create),
    path("read/<int:id>", views.read),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete),
]
