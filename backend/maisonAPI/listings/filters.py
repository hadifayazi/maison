import django_filters
from .models import Listing


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = ['city', 'state', 'zipcode', 'sale_type', 'price',
                  'bedrooms', 'bathrooms', 'house_type', 'surface']
