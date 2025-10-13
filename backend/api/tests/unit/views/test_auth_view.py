from django.test import TestCase, Client 
import inspect 
import importlib 
from rest_framework import views
from rest_framework_simplejwt.views import TokenObtainPairView

class TestAuthViews(TestCase):
    def setUp(self) -> None:
        self.client = Client() 
        
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_auth_custom_token_obtain_pair_view_exists(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        self.assertTrue(hasattr(module, "CustomTokenObtainPairView"))
    
    def test_if_custom_token_obtain_pair_view_is_a_class_api_view(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        self.assertTrue(issubclass(module.CustomTokenObtainPairView, TokenObtainPairView))