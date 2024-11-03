from rest_framework.authentication import BaseAuthentication 
from rest_framework.exceptions import AuthenticationFailed 
from django.contrib.auth.models import User

class CustomKeyAuthentication(BaseAuthentication): 
    def authenticate(self, request): 
        custom_key = request.query_params.get('custom_key') 
        if custom_key is None: 
            raise AuthenticationFailed('Ви не можете зайти!') 
        if custom_key != 'SecretKey': 
            raise AuthenticationFailed('Не той авторизаційний ключ') 
        try: 
            superadmin = User.objects.get(username='admin') 
            return (superadmin, None) 
        except User.DoesNotExist: 
            raise AuthenticationFailed('Не той користувач')