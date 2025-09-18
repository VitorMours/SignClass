from django.db import models
import uuid
from django.contrib.auth.models import User

NAMESPACE_SIGN = uuid.UUID('a67b938c-f09b-4e1a-8c31-4a11270b284e')

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
    
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(help_text="Coloque o nome do sinal que você está criando")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.FileField(help_text="Coloque o arquivo que deseja subir")
    knowledge_sector = models.CharField(choices=KNOWLEDGE_SECTOR_ENUM, help_text="De que área esse conhecimento é pertencente")