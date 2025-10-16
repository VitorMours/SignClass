from django.test import TestCase, Client
import importlib
import json
class TestAuthUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_auth_login_route_exists(self) -> None:
        response = self.client.post("/api/auth/login")
        self.assertEqual(response.status_code, 400)
        
    def test_if_auth_login_route_returns_not_found(self) -> None:
        response = self.client.get("/api/auth/login/")
        self.assertEqual(response.status_code, 404)
        
    def test_if_auth_login_route_return_forbidden_method(self) -> None:
        response = self.client.put("/api/auth/login")
        self.assertEqual(response.status_code, 405)
        
    def test_auth_login_response_with_body(self) -> None:
        data = {"email": "jvrezendemoura@gmail.com", "password": "32322916aA!"}
        response = self.client.post("/api/auth/login", 
                                json=data)
        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertEqual(response_data["status"], "success")
        self.assertIn("token", response_data)
        self.assertIn("user", response_data)
        
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