from django.shortcuts import render

from ghibliapp.models import Movie


def movies_list(request):
    movie_list = []
    for movie in Movie.objects.all():
        movie_list.append(
            {
                'movie': movie,
                'people': movie.person_set.all()
            }
        )
    context = {'movie_list': movie_list}

    return render(request, 'movies/movies_list.html', context)
