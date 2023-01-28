from django.contrib.auth.models import User
from rest_framework import authentication, exceptions


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        username = request.headers.get('Authorization')
        username = username.split(" ")[1]
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
