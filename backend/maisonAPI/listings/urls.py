from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateListingView.as_view(), name='list-create-listing'),
    path('<slug:slug>', views.RetrieveUpdateDestroyView.as_view(),
         name='retrieve-update-destroy-listing-slug'),
    path('<int:pk>', views.RetrieveUpdateDestroyView.as_view(),
         name='retrieve-update-destroy-listing-pk'),
]
