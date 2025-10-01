from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _

NAMESPACE_SIGN = uuid.UUID('a67b938c-f09b-4e1a-8c31-4a11270b284e')
    
class CustomUserManager(UserManager):
    def create_user(self, email, password, first_name, last_name=None, **extra_fields):
        if not email or not password or not first_name:
            raise ValueError(_("A required value was not passed"))
        
        email = self.normalize_email(email)
        

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
                
        user = self.model(
            first_name= first_name,
            last_name=last_name,
            email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, first_name, last_name=None, **extra_fields):
        if not email or not password or not first_name:
            raise ValueError(_("A required value was not passed"))
        
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField("email address", unique=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name","password")
    
    objects = CustomUserManager()    


class Sign(models.Model):

    ARTICULATION_POINT_CHOICES = {
            "TESTA": "testa",
            "BOCA": "boca",
            "TRONCO": "tronco",
            "NEUTRO": "neutro",
            "BRAÇO": "braço",
    }

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4())
    name = models.CharField(max_length=20, blank=False, null=False)
    meaning = models.CharField(max_length=125, blank=False, null=False)
    hand_configuration = models.URLField()
    articulation_point = models.CharField(choices=ARTICULATION_POINT_CHOICES)
    movement = models.CharField()   
    body_expression = models.CharField()
    direction_and_orientation = models.CharField()

    def __str__(self) -> str:
        return f"{self.name}: {self.meaning}"
    
    
    
class Video(models.Model):
    
    KNOWLEDGE_SECTOR_ENUM = [
        ("Exatas", "Ciências Exatas"),
        ("Humanas", "Ciências Humanas"),
        ("Linguagens", "Linguagens e suas tecnologias"),
        ("Natureza", "Ciências Naturais e suas Tecnologias"),
        ("Saúde", "Ciências da Saúde")
    ]
    
    id = models.UUIDField(primary_key=True, editable=False, unique = True, default = uuid.uuid4())
    name = models.CharField(help_text="Coloque o nome do sinal que você está criando")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    media = models.FileField(upload_to="uploads/", help_text="Coloque o arquivo que deseja subir")
    media_filename = models.CharField(max_length=255, blank=True, help_text="nome do arquivo que vai ficar dentro do banco de dados")
    knowledge_sector = models.CharField(choices=KNOWLEDGE_SECTOR_ENUM, help_text="De que área esse conhecimento é pertencente")
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE, help_text="Qual é o sinal do video", null=False, blank=False)
    
     
    def __str__(self) -> None:
        return f"[ {self.knowledge_sector} ] - {self.name}"
    
    
    