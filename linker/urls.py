from django.urls import path

from .views import index

urlpatterns = [
    path('<str:link_name>', index),
]
