from django.test import TestCase 
import inspect 
import importlib
from rest_framework import serializers
from django.contrib.auth import get_user_model 

User = get_user_model()

class TestSerializer(TestCase):
    
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
        