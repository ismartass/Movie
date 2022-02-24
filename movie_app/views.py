from django.shortcuts import render, get_object_or_404, reverse

# Create your views here.
from .models import Movie


def all_movies(request):
    movies_list = Movie.objects.all()
    context = {
        'movies': movies_list
    }
    return render(request, 'movie_app/all_movies.html', context=context)


def one_movie(request, id_movie: int):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'movie_app/one_movie.html',
                  {
                      'movie': movie
                  })




