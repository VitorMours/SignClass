from django.test import TestCase, Client
import importlib
from django.contrib.auth import get_user_model

class TestAuthUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.email_teste = "login@teste.com"
        self.senha_teste = "SenhaForte@123"
        self.user = get_user_model().objects.create_user(
            email=self.email_teste,
            password=self.senha_teste,
            first_name="Usuario",
            last_name="Login"
        )
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_auth_token_route_blocks_get_method(self) -> None:
        response = self.client.get("/api/auth/login")
        self.assertEqual(response.status_code, 405)
        
    def test_login_sucesso_retorna_tokens(self) -> None:
        login_data = {
            "email": self.email_teste,
            "password": self.senha_teste
        }
        response = self.client.post("/api/auth/login", data=login_data)
        
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn("access", response_data)
        self.assertIn("refresh", response_data)
        self.assertEqual(response_data["email"], self.email_teste)
        self.assertTrue("user_id" in response_data)

    def test_login_falha_com_senha_errada(self) -> None:
        login_data_errado = {
            "email": self.email_teste,
            "password": "SENHA_ERRADA"
        }
        response = self.client.post("/api/auth/login", data=login_data_errado)
        self.assertIn(response.status_code, [400, 401])

    def test_login_falha_com_usuario_inexistente(self) -> None:
        login_data_inexistente = {
            "email": "naoexiste@teste.com",
            "password": "qualquersenha"
        }
        response = self.client.post("/api/auth/login", data=login_data_inexistente)
        self.assertIn(response.status_code, [400, 401])

class TestUserUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_users_route_exists(self) -> None:
        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, 200)
        
    def test_if_users_route_block_wrong_http_verbs(self) -> None:
        put_response = self.client.put("/api/users")
        delete_response = self.client.delete("/api/users")
        self.assertEqual(put_response.status_code, 405)
        self.assertEqual(delete_response.status_code, 405)
        
    def test_if_user_route_returns_json(self) -> None:
        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        data = response.json()
        self.assertIsInstance(data, list)
    
    def test_if_single_user_route_exists(self) -> None:
        module = importlib.import_module("api.urls")
        url_patterns = module.urlpatterns
        exists = False
        for path in url_patterns:
            if path.name == "singular_user":
                exists = True
                break
        self.assertTrue(exists)

    def test_se_o_cadastro_de_usuario_funciona(self) -> None:
        user_data = {
            "email": "usuario_novo@teste.com",
            "password": "SenhaForte@123",
            "first_name": "Tester",
            "last_name": "QA"
        }
        user_count_before = get_user_model().objects.count()
        response = self.client.post("/api/users", data=user_data)
        
        self.assertEqual(response.status_code, 201)
        user_count_after = get_user_model().objects.count()
        self.assertEqual(user_count_after, user_count_before + 1)
        response_data = response.json()
        self.assertEqual(response_data['user']['email'], user_data['email'])

    def test_se_cadastro_falha_com_email_duplicado(self) -> None:
        get_user_model().objects.create_user(
            email="email.duplicado@teste.com",
            password="123",
            first_name="Usuario Original"
        )
        user_data_duplicada = {
            "email": "email.duplicado@teste.com",
            "password": "OutraSenha@123",
            "first_name": "Tentativa de Clone"
        }
        user_count_before = get_user_model().objects.count()
        response = self.client.post("/api/users", data=user_data_duplicada)
        self.assertEqual(response.status_code, 400)
        user_count_after = get_user_model().objects.count()
        self.assertEqual(user_count_after, user_count_before)