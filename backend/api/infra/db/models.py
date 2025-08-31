from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
import uuid

class Individual(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Campos de PermissionsMixin com related_name exclusivo
    groups = models.ManyToManyField(
        Group,
        related_name="individuals",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="individuals",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    

class Teatcher(Individual):
    is_staff= True    

class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    owner = models.ForeignKey(Individual, on_delete=models.CASCADE)
    path = models.URLField(max_length=255, blank=False, null=False)
    description = models.CharField(255, blank=True, null=False)