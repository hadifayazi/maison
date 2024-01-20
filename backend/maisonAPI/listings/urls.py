from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateListingView.as_view(), name='list-create-listing'),
    path('<>int:pk', views.RetrieveUpdateDestroyView.as_view(),
         'retrive-update-destroy-list',)
]
