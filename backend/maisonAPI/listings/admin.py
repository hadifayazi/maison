from django.contrib import admin
from .models import Listing


class AdminListing(admin.ModelAdmin):
    """
    Custom admin configuration for the Listing model.

    - `list_display`: Fields displayed in the list view.
    - `list_display_links`: Fields linked to the detail view in the list view.
    - `list_filter`: Filtering options on the right sidebar.
    - `list_editable`: Editable fields directly in the list view.
    - `search_fields`: Search box for searching records based on specified fields.
    - `list_per_page`: Number of items displayed per page in the list view.

    Additionally, includes 'is_published' in list_filter for filtering based on publication status.
    """
    list_display = ['id', 'title', 'realtor',
                    'price', 'list_date', 'is_published']
    list_display_links = ['id', 'title']
    list_filter = ['realtor', 'is_published']
    list_editable = ['is_published']
    search_fields = ['title', 'description', 'address',
                     'city', 'zipcode', 'city', 'state', 'price']
    list_per_page = 20


admin.site.register(Listing)
