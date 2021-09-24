from django.urls import path, include
from films.views import FilmCreateView, FilmsListView, FilmDetailView, TestView

urlpatterns = [
    path('create/', FilmCreateView.as_view(), name='create_film'),
    path('', FilmsListView.as_view(), name='films_list'),
    path('detail/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('test/', TestView.as_view(), name='film_custom_detail'),
]