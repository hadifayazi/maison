from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateRealtor.as_view(), name='realtors'),
    path('<int:pk>', views.RetrieveUpdateDestroyRealtorView.as_view(),
         name=('retrive-update-destroy-realtor')),
]
