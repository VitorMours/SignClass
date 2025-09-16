from django.test import TestCase
import importlib


class TestModels(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_teatcher_model_exists(self) -> None:
        models = importlib.import_module("api.models")
        self.assertTrue(hasattr(models, "Teatcher"))
        
        
    def test_if_teatcher_model_have_fields(self) -> None:
        teatcher_model_fields = 