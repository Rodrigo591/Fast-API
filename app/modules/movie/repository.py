from app.database.connection import collection
from bson import ObjectId

def create_movie(movie):
    result = collection.insert_one(movie)
    return str(result.inserted_id)

def get_movies():
    movies = []
    for m in collection.find():
        m["_id"] = str(m["_id"])
        movies.append(m)
    return movies

def get_movie(movie_id):
    movie = collection.find_one({"_id": ObjectId(movie_id)})
    if movie:
        movie["_id"] = str(movie["_id"])
    return movie

def update_movie(movie_id, movie):
    collection.update_one(
        {"_id": ObjectId(movie_id)},
        {"$set": movie}
    )
    return True

def delete_movie(movie_id):
    collection.delete_one({"_id": ObjectId(movie_id)})
    return True
