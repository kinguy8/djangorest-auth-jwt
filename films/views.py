from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

from films.serializers import FilmDetailSerializer, FilmsListSerializer
from films.models import Film
from films.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser


class FilmCreateView(generics.CreateAPIView):
    """VIEW FOR FILM'S CREATION PROCESS"""
    serializer_class = FilmDetailSerializer
    permission_classes = (IsAdminUser,)


class FilmsListView(generics.ListAPIView):
    """VIEW FOR FILM LIST"""
    serializer_class = FilmsListSerializer
    queryset = Film.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class FilmDetailView(generics.RetrieveUpdateDestroyAPIView):
    """VIEW FOR FILM DETAILS"""
    serializer_class = FilmDetailSerializer
    queryset = Film.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class TestView(APIView):
    """MY CUSTOM VIEW FOR FILM LIST"""

    def get(self, request, format=None):
        Films = Film.objects.all()
        serializer = FilmsListSerializer(Films, many=True)
        return Response(serializer.data)