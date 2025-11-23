from django.test import TestCase 
import inspect 
import importlib 
from rest_framework import views
from api.serializers import VideoSerializer, UserGetSerializer

class TestVideoViews(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_is_running(self) -> None:
        self.assertTrue(True)

    def test_if_video_view_exists(self) -> None:
        module = importlib.import_module("api.views.video_views")
        self.assertTrue(hasattr(module, "VideoView"))

    def tet_if_video_view_is_correct_subclass(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.VideoView           
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_video_view_have_get_method(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.VideoView
        self.assertTrue(hasattr(class_, "get"))
        
    def test_if_video_class_have_serializer_default_class(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.VideoView
        self.assertTrue(hasattr(class_, "serializer_class"))
        
    def test_if_video_view_serializer_class_is_correct(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.VideoView
        self.assertEqual(class_.serializer_class, VideoSerializer)    
    
    def test_if_video_get_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.VideoView
        signature = inspect.signature(class_.get)
        self.assertTrue("request" in signature.parameters.keys())
        
    def test_if_video_post_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.VideoView
        signature = inspect.signature(class_.post)
        self.assertTrue("request" in signature.parameters.keys())

class TestUserVideosView(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)

    def test_if_can_import_the_view(self) -> None:
        module = importlib.import_module("api.views.video_views")
        self.assertTrue(hasattr(module, "UserVideosView"))

    def test_if_view_have_the_correct_super_class(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.UserVideosView
        self.assertTrue(issubclass(class_, views.APIView))

    def test_if_view_have_serializer(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.UserVideosView
        self.assertTrue(hasattr(class_, "serializer_class"))

    def test_if_the_view_serializer_class_is_correct(self) -> None:
        module = importlib.import_module("api.views.video_views")
        class_ = module.UserVideosView
        self.assertTrue(class_.serializer_class, "UserVideosSerializer")
       


