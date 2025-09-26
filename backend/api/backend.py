from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import check_password
class EmailBackend(BaseBackend):
    """
        Authetication system based on the user email
        for the login and the register system be based on 
        the unique field inside of the database
    """
    def authenticate(self, request, email=None, password=None, token=None) -> None:
        try:
            if token is None:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    pass
                else:
                    return None


        except User.DoesNotExist:
            pass