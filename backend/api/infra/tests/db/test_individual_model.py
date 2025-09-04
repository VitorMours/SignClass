from api.infra.db.models import Individual
from django.test import TestCase 


class TestIndividualModel(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_user_creation(self) -> None:
        test_user = Individual.objects.create("")