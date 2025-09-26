from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import importlib
import api.models as model
import uuid
import inspect


class TestCustomUserManager(TestCase):
    def setUp(self) -> None:
        self.create_user_method_signature = ["self", "email", "password", "first_name", "last_name", "extra_fields"]

    def test_is_running(self) -> None:
        self.assertTrue(True)
    
    def test_if_model_is_importable(self) -> None:
        module = importlib.import_module("api.models")
        self.assertTrue(hasattr(module, "CustomUserManager"))
        
    def test_if_custom_user_manager_is_correct_subclass(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUserManager
        self.assertTrue(issubclass(class_, UserManager))   
    
    def test_if_custom_user_manager_have_create_user_method(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUserManager
        self.assertTrue(hasattr(class_, "create_user"))
        
    def test_if_cusmo_user_manager_have_create_superuser_method(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUserManager
        self.assertTrue(hasattr(class_, "create_superuser"))
    
    def test_if_custom_user_manager_create_user_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUserManager
        signature = inspect.signature(class_.create_user)
        actual_params = set(signature.parameters.keys())
        expected_params = set(self.create_user_method_signature)
        self.assertEqual(actual_params, expected_params)
        
    def test_if_can_create_user_with_create_user_method(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUserManager()
        custom_user = get_user_model()
        new_user = custom_user.objects.create_user("jvrezendemoura@gmail.com","32322016aA!","lucas")
        self.assertEqual(type(new_user), model.CustomUser)
    
    def testif_create_superuser_method_have_correct_signature(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUserManager
        signature = inspect.signature(class_.create_superuser)
        actual_params = set(signature.parameters.keys())
        expected_params = set(self.create_user_method_signature)
        self.assertEqual(actual_params, expected_params)
        
    def test_create_superuser_method_with_wrong_data(self) -> None:
        module = importlib.import_module("api.models")
        custom_user = get_user_model()
        new_super_user = custom_user.objects.create_superuser("vitor.lucas@gmail.com","32322916aA!","Vitor")
        self.assertEqual(type(new_super_user), model.CustomUser)
        self.assertTrue(new_super_user.is_superuser)
    
    
class TestUserModel(TestCase):
    def setUp(self) -> None:
        self.required_fields = ("first_name","password")
        
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_custom_user_model_exists_and_can_import(self) -> None:
        module = importlib.import_module("api.models")
        self.assertTrue(hasattr(module, "CustomUser"))
        
    def test_if_custom_user_is_abstract_user_sub_class(self) -> None:
        module = importlib.import_module("api.models")
        user_model = module.CustomUser
        self.assertTrue(issubclass(user_model, AbstractUser))
        self.assertTrue(issubclass(user_model, PermissionsMixin))
        
    def test_if_custom_user_have_the_required_field(self) -> None:
        module = importlib.import_module("api.models")
        user_model = model.CustomUser
        self.assertTrue(hasattr(user_model, "REQUIRED_FIELDS"))
        
    def test_if_custom_user_model_required_fields_are_correct(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUser
        self.assertEqual(self.required_fields, class_.REQUIRED_FIELDS)
        
    def test_if_string_representation_of_the_model_is_correct(self) -> None:
        module = importlib.import_module("api.models")
        class_ = module.CustomUser
        

class TestSignModel(TestCase):
    def setUp(self) -> None:
        self.sign_class_fields = ["id", "name", "meaning", "hand_configuration",
                  "articulation_point", "movement","body_expression","direction_and_orientation"]
        self.sign_instance = model.Sign.objects.create(
            name = "asdasd" ,
            meaning = "asdasd",
            hand_configuration = "https://gemini.google.com/app/e1225fbd754a1159",
            articulation_point = "testa",
            movement = "asdasd",
            body_expression = "asdasd",
            direction_and_orientation = "asdasd"
        )


    def test_if_import_models(self) -> None:
        module = importlib.import_module("api.models")
        self.assertTrue(hasattr(module, "Sign"))

    def test_if_class_module_have_all_fields(self) -> None: 
        for field in self.sign_class_fields:
            self.assertTrue(hasattr(model.Sign, field))

    def test_if_sign_model_fields_are_the_correct_field_type(self) -> None:
        self.assertIsInstance(model.Sign._meta.get_field("id"), models.UUIDField)
        self.assertIsInstance(model.Sign._meta.get_field("name"), models.CharField)
        self.assertIsInstance(model.Sign._meta.get_field("meaning"), models.CharField)
        self.assertIsInstance(model.Sign._meta.get_field("hand_configuration"), models.CharField)
        self.assertIsInstance(model.Sign._meta.get_field("articulation_point"), models.CharField)
        self.assertIsInstance(model.Sign._meta.get_field("movement"), models.CharField)
        self.assertIsInstance(model.Sign._meta.get_field("body_expression"), models.CharField)
        self.assertIsInstance(model.Sign._meta.get_field("direction_and_orientation"), models.CharField)

    def test_if_id_field_have_the_correct_especifications(self) -> None:
        self.assertEqual(model.Sign._meta.get_field("id").unique, True)
        self.assertEqual(model.Sign._meta.get_field("id").editable, False)

    def test_if_name_field_have_the_correct_especifications(self) -> None:
        self.assertEqual(model.Sign._meta.get_field("name").blank, False)
        self.assertEqual(model.Sign._meta.get_field("name").null, False)
        self.assertEqual(model.Sign._meta.get_field("name").max_length, 20)
        
    def test_if_meaning_field_have_the_correct_especifications(self) -> None:
        self.assertEqual(model.Sign._meta.get_field("meaning").blank, False)
        self.assertEqual(model.Sign._meta.get_field("meaning").null, False)
        self.assertEqual(model.Sign._meta.get_field("meaning").max_length, 125)

    def test_if_hand_configuration_have_the_correct_especifications(self) -> None:
        pass 

    def test_if_articulation_point_have_the_correct_configurations(self) -> None:
        self.assertTrue(hasattr(model.Sign._meta.get_field("articulation_point"), "choices"))
        self.assertTrue(model.Sign._meta.get_field("articulation_point").choices)
        self.assertEqual(len(model.Sign._meta.get_field("articulation_point").choices), 5)
        self.assertEqual(model.Sign._meta.get_field("articulation_point").blank, False)
        self.assertEqual(model.Sign._meta.get_field("articulation_point").null, False)
    
    
    def test_if_sign_have_str_representation(self) -> None:
        self.assertTrue(str(self.sign_instance), f"{self.sign_instance.name}: {self.sign_instance.meaning}")
        
        
class TestVideoModel(TestCase):
    def setUp(self) -> None:
        self.model_fields = ["id","name","owner","media","knowledge_sector"]
        
    def test_if_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_model_exists(self) -> None: 
        module = importlib.import_module("api.models")
        self.assertTrue(hasattr(module, "Video"))
        
    def test_if_video_class_is_a_model(self) -> None:
        video = model.Video 
        self.assertTrue(issubclass(video, models.Model))
        
    def test_if_model_have_the_necessary_fields(self) -> None:
        for field in self.model_fields:
            self.assertTrue(hasattr(model.Video, field))
            
    def test_if_model_have_knowledge_sector_enum(self) -> None:
        module = importlib.import_module("api.models")
        self.assertTrue(hasattr(module.Video, "KNOWLEDGE_SECTOR_ENUM"))
    
    def test_if_model_fields_are_from_the_correct_type(self) -> None:
        self.assertIsInstance(model.Video._meta.get_field("id"), models.UUIDField)
        self.assertIsInstance(model.Video._meta.get_field("name"), models.CharField)
        self.assertIsInstance(model.Video._meta.get_field("owner"), models.ForeignKey)
        self.assertIsInstance(model.Video._meta.get_field("media"), models.FileField)
        self.assertIsInstance(model.Video._meta.get_field("knowledge_sector"), models.CharField)

    def test_if_model_media_have_the_correct_config(self) -> None:
        self.assertTrue(model.Video._meta.get_field("media").help_text == "Coloque o arquivo que deseja subir")
        
    def test_if_model_name_field_have_correct_config(self) -> None:
        pass
    
    def test_if_model_owner_field_have_the_correct_config(self) -> None:
        self.assertTrue(model.Video._meta.get_field("sign").help_text, "Qual é o sinal do video")
    
    def test_if_knowledge_sector_fields_is_choices(self) -> None:
        self.assertTrue(model.Video._meta.get_field("knowledge_sector").choices)
        
    def test_if_knowledge_sector_choice_is_correct(self) -> None:
        choices = model.Video.KNOWLEDGE_SECTOR_ENUM
        self.assertEqual(model.Video._meta.get_field("knowledge_sector").choices, choices)
    
    def test_if_all_model_fields_have_help_text(self) -> None:
        model_fields = model.Video._meta.get_fields()
        for field in model_fields:
            if field.name == "id" or field.name == "owner":
                continue
            self.assertNotEqual(field.help_text, '', f"O campo {field.name} nao possui help text")
            
    def test_if_class_id_have_unique_configuration(self) -> None:
        video_model = model.Video()
        self.assertTrue(model.Video._meta.get_field("id").unique)
    
    
