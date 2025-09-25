from django.test import TestCase
from django.contrib.auth.backends import BaseBackend
import importlib
import inspect

class TestEmailBackend(TestCase):
    def setUp(self) -> None:
        self.required_authentication_function_parameters = [
            "self",
            "request",
            "email",
            "password",
            "token"
        ] 
    
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_file_have_email_backend(self) -> None:
        module = importlib.import_module("api.backend")
        self.assertTrue(hasattr(module, "EmailBackend"))
        
    def test_if_email_backend_have_correct_inheretance(self) -> None:
        module = importlib.import_module("api.backend")
        class_ = module.EmailBackend
        self.assertTrue(issubclass(class_, BaseBackend))
        
    def test_if_email_backend_have_the_method(self) -> None:
        module = importlib.import_module("api.backend")
        class_ = module.EmailBackend
        self.assertTrue(hasattr(class_, "authenticate"))            
        self.assertTrue(callable(class_.authenticate))
        
    def test_if_email_backend_have_the_correct_signature(self) -> None:
        module = importlib.import_module("api.backend")
        class_ = module.EmailBackend 
        signature = inspect.signature(class_.authenticate)
        
        for parameter in signature.parameters.keys():
            self.assertTrue(parameter in self.required_authentication_function_parameters) 
        
        for parameter in self.required_authentication_function_parameters:
            self.assertTrue(parameter in signature.parameters.keys()) 
            