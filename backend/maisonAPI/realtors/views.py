from django.shortcuts import render
from .models import Realtor
from .serializers import RealtorSerializer
from rest_framework import permissions, generics


class ListCreateRealtor(generics.ListCreateAPIView):
    """API endpoint that allows the creation and listing of realtors."""
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class RetrieveUpdateDestroyRealtorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
