from django.test import TestCase, Client
import importlib
import json
class TestAuthUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_auth_token_route_exists(self) -> None:
        response = self.client.post("/api/auth/login")
        self.assertEqual(response.status_code, 400)
        
    def test_if_auth_token_route_returns_not_found(self) -> None:
        response = self.client.get("/api/auth/login/")
        self.assertEqual(response.status_code, 404)
        
    def test_if_auth_token_return_200_sucess_in_message(self) -> None:
        pass 
    
    def test_if_signin_route_exists(self) -> None:
        response = self.client.get("/api/auth/signup")
        self.assertEqual(response.status_code, 405)

    def test_if_signin_route_can_return_not_found(self) -> None:
        response = self.client.get("/api/auth/signup/")
        self.assertEqual(response.status_code, 404)
        
    def test_if_can_pass_data_in_body_for_signin_route(self) -> None:
        pass


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
        
        
class TestVideoUrls(TestCase): 
    def setUp(self) -> None:
        self.client = Client() 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_call_url(self) -> None:
        response = self.client.get("/api/videos")
        self.assertEqual(response.status_code, 200)
    
    def test_if_can_post_url_without_body(self) -> None:
        response = self.client.post("/api/videos")
        self.assertEqual(response.status_code, 400)
    
    def test_if_can_post_url_with_body(self) -> None:
        pass
    
    def test_if_can_update_the_url(self) -> None:
        response = self.client.put("/api/videos")
        self.assertEqual(response.status_code, 405)
        
    def test_if_can_delete_the_url(self) -> None:
        response = self.client.delete("/api/videos")
        self.assertEqual(response.status_code, 405)

class TestSignUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client() 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_get_app_the_signs(self) -> None:
        response = self.client.get("/api/signs")
        self.assertEqual(response.status_code, 200)

    def test_if_other_http_methods_return_error(self) -> None:
        response_put = self.client.put("/api/signs")
        self.assertEqual(response_put.status_code, 405)
        response_delete = self.client.delete("/api/signs")
        self.assertEqual(response_delete.status_code, 405)

    


    

        
