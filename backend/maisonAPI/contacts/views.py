from .models import Contact
from .serializers import ContactSerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.core.mail import send_mail


class ContactCreateView(generics.CreateAPIView):
    """View to create new contact and send email."""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Send email when a new contact is created
        send_mail(
            'New Contact Form Submission',
            f'Name: {serializer.validated_data["name"]}\nEmail: {serializer.validated_data["email"]}\nSubject: {serializer.validated_data["subject"]}\nMessage: {serializer.validated_data["message"]}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_TO],
            fail_silently=False,
        )
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'success': 'Email sent successfully.'}, status=status.HTTP_201_CREATED)
