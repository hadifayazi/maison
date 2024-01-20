from django.db import models
from realtors.models import Realtor
from django.utils import timezone


class ListingImage(models.Model):
    """Listing images."""
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')


class Listing(models.Model):
    """Model representing a house/apartment to rent or sale"""
    class SaleType(models.TextChoices):
        FOR_SALE = 'For sale'
        FOR_RENT = 'For rent'

    class HouseType(models.TextChoices):
        MAISON = 'Maison'
        APPARTEMENT = 'Apartment'
        VILLA = 'Villa'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    sale_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_type = models.CharField(
        max_length=50, choices=HouseType.choices, default=HouseType.APPARTEMENT)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ManyToManyField(ListingImage, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title
