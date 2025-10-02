from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model 
from django.contrib.auth.hashers import check_password

User = get_user_model()

class EmailBackend(BaseBackend):
    """
        Authetication system based on the user email
        for the login and the register system be based on 
        the unique field inside of the database
    """
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email = email)
            
            password_check = check_password(user.password, password)
            if password_check:
                return user             

        except User.DoesNotExist:
            return None            
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None