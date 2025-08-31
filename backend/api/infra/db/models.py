from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
import uuid

class Individual(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    last_login = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Teatcher(Individual):
    is_staff= True    

class Video(models.Model):
    AREA_CHOICES = [
        ("Ling","Linguagens"),
        ("Math","Matematica"),
        ("Humn","Humanidades"),
        ("Natr","Natureza"),
        ("Saud","Saude e Qualidade de Vida")
    ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    path = models.URLField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=False)
    owner = models.ForeignKey(Individual, on_delete=models.CASCADE)
    knowledge_sector = models.CharField(max_length=4, null=False, blank=False, choices=AREA_CHOICES)

    def __str__(self) -> None:
        return f"{self.name}: {self.description} - {self.owner.first_name} {self.owner.last_name}"


class Knowledge(models.Model):
    pass