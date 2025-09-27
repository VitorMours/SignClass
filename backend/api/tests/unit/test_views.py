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
        
    def test_if_user_view_have_get_method(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserView
        self.assertTrue(hasattr(class_, "get"))        
        
    def test_if_get_user_view_receive_request(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserView
        signature = inspect.signature(class_.get)
        self.assertTrue("request" in signature.parameters.keys())  
        
    def test_if_user_view_have_post_method(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserView 
        self.assertTrue(hasattr(class_, "post"))
        
    def test_if_user_view_post_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserView
        signature = inspect.signature(class_.post)
        self.assertTrue("request" in signature.parameters.keys())