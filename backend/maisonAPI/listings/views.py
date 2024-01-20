from django.shortcuts import render
from .models import Listing, ListingImage
from .serializers import ListingSerializer, ListingDetailSerializer, ListingImageSerializer
from rest_framework import generics, permissions


class ListCreateListingView(generics.ListCreateAPIView):
    """
    View for listing creation and retrieval.

    - For `GET` requests, retrieves a list of listings.
    - For `POST` requests, creates a new listing.

    Permissions:
    - For `GET`: Allow any user (public access).
    - For `POST`: Requires admin user.

    Serializer:
    - For `GET`: Uses `ListingSerializer`.
    - For `POST`: Uses `ListingDetailSerializer`.
    """
    queryset = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ListingDetailSerializer
        return ListingSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
