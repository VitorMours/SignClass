from django.test import TestCase, Client 
import importlib 
import inspect 
import json

class TestAuthIntegration(TestCase):
    def setUp(self) -> None:
        self.client = Client() 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
        
    def test_login_user_with_login_endpoint(self) -> None:
        pass 
        # TODO: Need to cerate the user in the database and after this, we need to populate the database