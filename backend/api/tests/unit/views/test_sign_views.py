from django.test import TestCase 
import inspect 
import importlib 
from rest_framework import views
from api.serializers import SignSerializer, VideoSerializer, UserGetSerializer

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
        


class TestSignDetailViews(TestCase):
    def setUp(self) -> None:
        self.get_method_signature = ["self", "request", "pk", "format"]
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
    
    def test_if_can_import_sign_detail_view(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        self.assertTrue(hasattr(module, "SignDetailView"))
        
        
    def test_if_detail_sign_view_is_an_api_view_subclass(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignDetailView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_detail_sign_view_have_serializer_class(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignDetailView
        self.assertTrue(hasattr(class_, "serializer_class"))
        
    def test_if_detail_sign_view_have_correct_serializer_class(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignDetailView
        self.assertIs(class_.serializer_class, SignSerializer)
        
    def test_if_detail_sign_vie_have_the_get_method(self) -> None:
        module = importlib.import_module("api.views.sign_views")
        class_ = module.SignDetailView
        self.assertTrue(class_, "get")
        
    def test_if_the_get_method_have_the_correct_signature(self) -> None:
        """
        Verifica se os nomes e a ordem dos parâmetros do método get estão corretos.
        """
        try:
            module = importlib.import_module("api.views.sign_views")
            class_ = module.SignDetailView
        except (ImportError, AttributeError) as e:
            self.fail(f"Não foi possível importar a view: {e}")

        signature = inspect.signature(class_.get)
        actual_signature_names = list(signature.parameters.keys())

        self.assertEqual(
            actual_signature_names, 
            self.get_method_signature,
            f"A assinatura do método 'get' não corresponde ao esperado. "
            f"Esperado: {self.get_method_signature}, "
            f"Recebido: {actual_signature_names}"
        )



    