from django.shortcuts import render
from .models import Listing, ListingImage
from .serializers import ListingSerializer, ListingDetailSerializer, ListingImageSerializer
from rest_framework import generics, permissions
from .filters import ListingFilter
import django_filters


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

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ListingFilter


class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single listing.

    - For `GET` requests, retrieves details for a specific listing.
    - For `PUT`, `PATCH`, and `DELETE` requests, requires admin user permissions.

    Serializer:
    - Uses `ListingDetailSerializer` for detailed representation.

    Lookup Field:
    - Supports both `pk` (primary key) and `slug` as lookup options.
      If `slug` is provided in the URL, it's used for the lookup; otherwise, falls back to `pk`.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
