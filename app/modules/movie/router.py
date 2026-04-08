from fastapi import APIRouter
from app.modules.movie.schema import Movie
from app.modules.movie import service

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/")
def create(movie: Movie):
    return {"id": service.create_movie(movie.dict())}

@router.get("/")
def read_all():
    return service.get_movies()

@router.get("/{movie_id}")
def read_one(movie_id: str):
    return service.get_movie(movie_id)

@router.put("/{movie_id}")
def update(movie_id: str, movie: Movie):
    service.update_movie(movie_id, movie.dict())
    return {"message": "Updated"}

@router.delete("/{movie_id}")
def delete(movie_id: str):
    service.delete_movie(movie_id)
    return {"message": "Deleted"}
