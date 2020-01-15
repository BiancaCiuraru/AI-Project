from imdb import IMDb

ia = IMDb()


def get_description_genre(movie_name):
    movie = ia.search_movie(movie_name)
    id_movie = movie[0].movieID

    movie_info = ia.get_movie(id_movie)
    genres = ''
    for genre in movie_info['genres']:
        genres += genre + ', '

    description = movie_info.get('plot outline')
    return genres[:-2], description

# print(get_description_genre('Jumanji'))
