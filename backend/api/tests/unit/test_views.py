from django.test import TestCase 
import inspect 
import importlib 
from rest_framework import views
from api.serializers import VideoSerializer, UserGetSerializer

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
        
    def test_if_views_have_sign_views(self) -> None:
        module = importlib.import_module("api.views")
        self.assertTrue(hasattr(module, "SignView"))
        
    def test_if_sign_view_is_api_view_subclass(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.SignView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_sign_views_have_get_method(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.SignView
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_sign_view_get_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.SignView
        signature = inspect.signature(class_.get)
        self.assertTrue("request" in signature.parameters.keys())
        
    def test_if_sign_view_have_post_method(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.SignView
        self.assertTrue(hasattr(class_, "post"))
        
    def test_if_sign_view_post_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.SignView
        signature = inspect.signature(class_.post)
        self.assertTrue("request" in signature.parameters.keys())
        
    def test_if_video_view_exists(self) -> None:
        module = importlib.import_module("api.views")
        self.assertTrue(hasattr(module, "VideoView"))

    def tet_if_video_view_is_correct_subclass(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.VideoView           
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_video_view_have_get_method(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.VideoView
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_video_class_have_serializer_default_class(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.VideoView
        self.assertTrue(hasattr(class_, "serializer_class"))
        
    def test_if_video_view_serializer_class_is_correct(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.VideoView
        self.assertEqual(class_.serializer_class, VideoSerializer)    
    
    def test_if_video_get_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.VideoView
        signature = inspect.signature(class_.get)
        self.assertTrue("request" in signature.parameters.keys())
        
    def test_if_video_post_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.VideoView
        signature = inspect.signature(class_.post)
        self.assertTrue("request" in signature.parameters.keys())


class TestUserViews(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_user_detail_view_exists(self) -> None:
        module = importlib.import_module("api.views")
        self.assertTrue(hasattr(module, "UserDetailView"))
        
    def test_if_user_detail_view_is_usable(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserDetailView
        self.assertTrue(callable(class_))
        
    def test_if_user_detail_view_is_the_correct_sub_class(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserDetailView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_user_detail_view_have_serializer_class_variable(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserDetailView
        self.assertTrue(hasattr(class_, "serializer_class"))
        
    def test_if_user_detail_view_serializer_class_is_correct(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserDetailView
        self.assertIs(class_.serializer_class, UserGetSerializer)
        self.assertTrue(True) # Modificar
        
        
    def test_if_user_detail_view_have_get_method(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserDetailView
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_get_request_have_correct_method_signature(self) -> None:
        required_fields = ["request","pk","format","self"]
        module = importlib.import_module("api.views")
        class_ = module.UserDetailView
        signature = inspect.signature(class_.get)
        
        for keys in signature.parameters.keys():
            if keys in required_fields:
                required_fields.remove(keys)

        self.assertListEqual(required_fields, [])
            
    # TODO: Fazer os testes necessarios da classe para prevenir os problemas,
    # tipo post, proibido de fazer        
