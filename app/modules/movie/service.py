from app.modules.movie import repository

def create_movie(movie):
    return repository.create_movie(movie)

def get_movies():
    return repository.get_movies()

def get_movie(movie_id):
    return repository.get_movie(movie_id)

def update_movie(movie_id, movie):
    return repository.update_movie(movie_id, movie)

def delete_movie(movie_id):
    return repository.delete_movie(movie_id)
