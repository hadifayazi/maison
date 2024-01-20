from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateRealtor.as_view(), name='realtors'),
]
