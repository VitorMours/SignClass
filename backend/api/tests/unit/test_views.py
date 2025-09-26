from django.test import TestCase 
import inspect 
import importlib 
from rest_framework import views
class TestViews(TestCase):
    def setUp(self) -> None:
        
        pass 
    
    def test_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_user_view_exists(self) -> None: 
        module = importlib.import_module("api.views")
        self.assertTrue(hasattr(module, "UserView"))
        
    def test_if_user_view_is_a_api_view(self) -> None: 
        module = importlib.import_module("api.views")
        self.assertTrue(issubclass(module.UserView, views.APIView))