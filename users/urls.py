from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import CookieTokenObtainPairView, LogoutCookieView, CookieTokenRefreshView

urlpatterns = [
    path('login/', CookieTokenObtainPairView.as_view()),
    path('refresh/', CookieTokenRefreshView.as_view()),
    path('logout/', LogoutCookieView.as_view())
]
