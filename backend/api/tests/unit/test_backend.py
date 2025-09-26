from django.test import TestCase, RequestFactory
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

import importlib
import inspect

class TestEmailBackend(TestCase):
    def setUp(self) -> None:
        self.request = RequestFactory()
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
            
    def test_if_authenticate_user_with_wrong_data(self) -> None:
        request = self.request.post("api/auth/token/")
        module = importlib.import_module("api.backend")
        class_ = module.EmailBackend()
        result = class_.authenticate(request, email="b@b.com", password="tentadenovo123")
        self.assertIsNone(result)
            
    def test_if_authenticate_user_that_exists(self) -> None:
        request = self.request.post("api/auth/token")
        User = get_user_model()
        new_user = User.objects.create(
            first_name="joao",
            last_name="moura",
            email="jvrezendemoura@gmail.com",
            password="32322916aA!"
        )
        new_user.save()
        module = importlib.import_module("api.backend")
        class_ = module.EmailBackend()
        result = class_.authenticate(request, email="jvrezendemoura@gmail.com", password="32322916aA!")
        print(result)