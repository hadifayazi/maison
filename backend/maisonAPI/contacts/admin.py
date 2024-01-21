from django.contrib import admin
from .models import Contact


class AdminContact(admin.ModelAdmin):
    """
    Custom admin configuration for the Contact model.

    - `list_display`: Fields displayed in the list view.
    - `list_display_links`: Fields linked to the detail view in the list view.
    - `search_fields`: Search box for searching records based on specified fields.
    - `list_per_page`: Number of items displayed per page in the list view.
    """
    list_display = ['id', 'name', 'email', 'subject']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email', 'subject']
    list_per_page = 20


admin.site.register(Contact, AdminContact)
