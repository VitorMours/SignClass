from django.test import TestCase 
import inspect 
import importlib 
from rest_framework import views
from api.serializers import VideoSerializer, UserGetSerializer

class TestUserViews(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_user_detail_view_exists(self) -> None:
        module = importlib.import_module("api.views.user_views")
        self.assertTrue(hasattr(module, "UserDetailView"))
        
    def test_if_user_detail_view_is_usable(self) -> None:
        module = importlib.import_module("api.views.user_views")
        class_ = module.UserDetailView
        self.assertTrue(callable(class_))
        
    def test_if_user_detail_view_is_the_correct_sub_class(self) -> None:
        module = importlib.import_module("api.views.user_views")
        class_ = module.UserDetailView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_user_detail_view_have_serializer_class_variable(self) -> None:
        module = importlib.import_module("api.views.user_views")
        class_ = module.UserDetailView
        self.assertTrue(hasattr(class_, "serializer_class"))
        
    def test_if_user_detail_view_serializer_class_is_correct(self) -> None:
        module = importlib.import_module("api.views.user_views")
        class_ = module.UserDetailView
        self.assertIs(class_.serializer_class, UserGetSerializer)
        self.assertTrue(True) # Modificar
        
        
    def test_if_user_detail_view_have_get_method(self) -> None:
        module = importlib.import_module("api.views.user_views")
        class_ = module.UserDetailView
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_get_request_have_correct_method_signature(self) -> None:
        required_fields = ["request","pk","format","self"]
        module = importlib.import_module("api.views.user_views")
        class_ = module.UserDetailView
        signature = inspect.signature(class_.get)
        
        for keys in signature.parameters.keys():
            if keys in required_fields:
                required_fields.remove(keys)

        self.assertListEqual(required_fields, [])
            
    # TODO: Fazer os testes necessarios da classe para prevenir os problemas,
    # tipo post, proibido de fazer        
