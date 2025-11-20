from django.test import TestCase 
import inspect 
import importlib 
from rest_framework import views
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.serializers import VideoSerializer, UserGetSerializer


class TestSignViews(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_views_have_sign_views(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        self.assertTrue(hasattr(module, "SignView"))
        
    def test_if_sign_view_is_api_view_subclass(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_sign_views_have_get_method(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_sign_view_get_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView
        signature = inspect.signature(class_.get)
        self.assertTrue("request" in signature.parameters.keys())
        
    def test_if_sign_view_have_post_method(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView
        self.assertTrue(hasattr(class_, "post"))
        
    def test_if_sign_view_post_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView
        signature = inspect.signature(class_.post)
        self.assertTrue("request" in signature.parameters.keys())

    def test_if_sign_view_have_authentication_classes(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView 
        self.assertTrue(hasattr(class_, "authentication_classes"))
       
    def test_if_sign_view_have_authentication_classes(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView.authentication_classes 
        self.assertIn(JWTAuthentication, class_)
       


    def test_if_sign_view_have_permission_classes(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignView 
        self.assertTrue(hasattr(class_, "permission_classes"))        
        
class TestUserSignDetailedView(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_views_have_user_sign_detailed_view(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        self.assertTrue(hasattr(module, "UserSignDetailedView"))
        
    def test_if_user_sign_detailed_view_is_api_view_subclass(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.UserSignDetailedView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_user_sign_detailed_view_have_authentication_classes(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.UserSignDetailedView 
        self.assertTrue(hasattr(class_, "authentication_classes"))
       
    def test_if_user_sign_detailed_view_have_authentication_classes(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.UserSignDetailedView.authentication_classes 
        self.assertIn(JWTAuthentication, class_)
       
    def test_if_user_sign_detailed_view_have_permission_classes(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.UserSignDetailedView 
        self.assertTrue(hasattr(class_, "permission_classes"))
        
    def test_if_user_sign_detailed_view_have_get_method(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.UserSignDetailedView
        self.assertTrue(hasattr(class_, "get"))
    
    def test_if_user_sign_detailed_view_get_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.UserSignDetailedView
        signature = inspect.signature(class_.get)
        self.assertTrue("request" in signature.parameters.keys())
        self.assertTrue("pk" in signature.parameters.keys())

    
    

    
