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
        
        
        
class TestSignUpView(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_signup_view(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        self.assertTrue(module)
        
    def test_if_signup_view_class_exists(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        self.assertTrue(hasattr(module, "SignUpView"))
        
    def test_if_signup_view_is_a_api_view_sub_class(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        class_ = module.SignUpView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_view_have_post_method(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        class_ = module.SignUpView 
        self.assertTrue(hasattr(class_, "post"))
        
    def test_is_post_sign_up_view_method_have_required_parameters(self) -> None:
        module = importlib.import_module("api.views.auth_views")
        class_ = module.SignUpView
        signature = inspect.signature(class_.post)
        self.assertIn("self", signature.parameters.keys())
        self.assertIn("request", signature.parameters.keys())
        self.assertIn("format", signature.parameters.keys())
        
    
    