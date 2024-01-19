from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(UserManager):
    """Custom Manager to handle creating of users"""

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email=email)
        user = self.model(email,  **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def creat_superuser(self, email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
