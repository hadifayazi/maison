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
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

    def get_object(self):
        lookup_field = self.lookup_field
        if lookup_field in self.kwargs:
            return self.queryset.get(**{lookup_field: self.kwargs[lookup_field]})
        return super().get_object()

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
