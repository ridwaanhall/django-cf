from django.urls import path
from . import views


urlpatterns = [
    path('', views.SimpleJsonView.as_view(), name='simple_json'),
]
