from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies),
    path('movie/<int:id_movie>', views.one_movie, name='movie_info'),


]