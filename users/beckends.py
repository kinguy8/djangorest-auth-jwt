from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import authentication
from rest.settings import JWT_AUTH_REFRESH_COOKIE
from django.contrib.auth import get_user_model


class CookieJWTAuthentication(authentication.BaseAuthentication):
    """RETURNS THE USER IF TOKEN IS IN HEADER OR IN COOKIE"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = get_user_model()

    def authenticate(self, request):
        if JWT_AUTH_REFRESH_COOKIE in request.COOKIES:
            raw_token = request.COOKIES[JWT_AUTH_REFRESH_COOKIE]
            if raw_token is None:
                return None
        else:
            header = JWTAuthentication.get_header(self, request)
            if header is None:
                return None
            raw_token = JWTAuthentication.get_raw_token(self, header)
            if raw_token is None:
                return None
        validated_token = JWTAuthentication.get_validated_token(self, raw_token)

        return JWTAuthentication.get_user(self, validated_token), validated_token