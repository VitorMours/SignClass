from django.test import TestCase 
import inspect 
import importlib
from rest_framework import serializers
from django.contrib.auth import get_user_model 

User = get_user_model()

class TestUserSerializer(TestCase):
    
    def setUp(self) -> None:
        pass
    def test_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_the_serializer_module(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(hasattr(module, "UserSerializer"))    
    
    def test_if_user_serializer_is_serializer_subclass(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(issubclass(module.UserSerializer, serializers.ModelSerializer))
    
    def test_user_serializer_meta_fields(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.UserSerializer
        self.assertTrue(hasattr(class_, 'Meta'))
        self.assertTrue(hasattr(class_.Meta, 'model'))
        self.assertTrue(hasattr(class_.Meta, 'fields'))
        
        
class TestGetUserSerializer(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_class_is_from_the_correct_subclass(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(issubclass(module.UserGetSerializer, serializers.ModelSerializer))        
        
    def test_user_get_serializer_meta_fields(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.UserGetSerializer
        self.assertTrue(hasattr(class_, 'Meta'))
        self.assertTrue(hasattr(class_.Meta, 'model'))
        self.assertTrue(hasattr(class_.Meta, 'fields'))
        
        
class TestSignSerializer(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_serializer_is_importable(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(hasattr(module, "SignSerializer"))
        
    def test_if_class_is_from_the_correct_subclass(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.SignSerializer
        self.assertTrue(issubclass(class_, serializers.ModelSerializer))
        
    def test_if_class_have_meta_configuration_and_model(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.SignSerializer
        self.assertTrue(hasattr(class_, 'Meta'))
        self.assertTrue(hasattr(class_.Meta, 'model'))
        self.assertTrue(hasattr(class_.Meta, 'fields'))
        
class TestGetSignSerializer(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_serializer_is_importable(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(hasattr(module, "SignGetSerializer"))
        
    def test_if_class_is_from_the_correct_subclass(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.SignGetSerializer
        self.assertTrue(issubclass(class_, serializers.ModelSerializer))
        
    def test_if_class_have_meta_configuration_and_model(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.SignGetSerializer
        self.assertTrue(hasattr(class_, 'Meta'))
        self.assertTrue(hasattr(class_.Meta, 'model'))
        self.assertTrue(hasattr(class_.Meta, 'fields'))
        
        
        
class TestVideoSerializer(TestCase):
    def setUp(self) -> None:
        pass
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_video_serializer(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(hasattr(module, "VideoSerializer"))
        
    def test_if_video_serializer_is_correct_subclass(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(issubclass(module.VideoSerializer, serializers.ModelSerializer))
        
    def test_if_video_serializer_have_meta_class(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.VideoSerializer
        self.assertTrue(hasattr(class_, "Meta"))
        
    def test_if_media_filename_is_read_only(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.VideoSerializer
        readonly_list = class_.Meta.read_only_fields
        self.assertTrue("media_filename" in readonly_list)
        
        
    def test_if_meta_class_have_the_correct_configuration(self) -> None: 
        module = importlib.import_module("api.serializers")
        class_ = module.VideoSerializer
        self.assertTrue(hasattr(class_, 'Meta'))
        self.assertTrue(hasattr(class_.Meta, 'model'))
        self.assertTrue(hasattr(class_.Meta, 'fields'))
        
class TestVideoGetSerializer(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_class_exists_in_module(self) -> None:
        module = importlib.import_module("api.serializers")
        self.assertTrue(hasattr(module, "VideoGetSerializer"))
        
    def test_if_class_is_correct_subclass(self) -> None: 
        module = importlib.import_module("api.serializers")
        class_ = module.VideoGetSerializer
        self.assertTrue(issubclass(class_, serializers.ModelSerializer))
        
    def test_if_class_have_correct_meta_fields(self) -> None:
        module = importlib.import_module("api.serializers")
        class_ = module.VideoGetSerializer
        self.assertTrue(hasattr(class_, 'Meta'))
        self.assertTrue(hasattr(class_.Meta, 'model'))
        self.assertTrue(hasattr(class_.Meta, 'fields'))
        