from api.infra.db.models import Individual
from django.test import TestCase 


class TestIndividualModel(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_user_create(self) -> None:
        test_user = Individual.objects.create(
            first_name = "Vitor",
            last_name = "Lucas",
            email = "vitor.lucas@email.com",
            password = "32322916aA!",
            is_active = True,
            )
        
        self.assertIsInstance(test_user, Individual, "Testando tipo primitivo da criação do usuário")