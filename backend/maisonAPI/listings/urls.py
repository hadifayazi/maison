from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateListingView.as_view(), name='list-create-listing'),
]
