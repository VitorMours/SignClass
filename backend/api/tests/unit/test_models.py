from django.test import TestCase 
from django.db import models
import importlib
import api.models as model
import uuid

class TestModels(TestCase):
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