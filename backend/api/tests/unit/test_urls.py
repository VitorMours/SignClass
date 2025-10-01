from django.test import TestCase, Client


class TestAuthUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_auth_token_route_exists(self) -> None:
        response = self.client.get("/api/auth/token/")
        self.assertEqual(response.status_code, 405)
        
    def test_if_auth_token_route_redirect_correctly(self) -> None:
        response = self.client.get("/api/auth/token")
        self.assertEqual(response.status_code, 301)
        
        
# Lucas
class TestUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_users_route_exists(self) -> None:
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        
    def test_if_users_route_block_wrong_http_verbs(self) -> None:
        put_response = self.client.put("/api/users/")
        delete_response = self.client.delete("/api/users/")
        self.assertEqual(put_response.status_code, 405)
        self.assertEqual(delete_response.status_code, 405)
        
    def test_if_user_route_returns_json(self) -> None:
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        data = response.json()
        self.assertIsInstance(data, list)