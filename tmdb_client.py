import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzA4MDM3OGY5OTBhMTRhY2ZlZGFhOWYzNGJhM2I2NiIsInN1YiI6IjVmMmZhMmYxM2MzYWIwMDAzNDQ5NzdhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wtiKJS3SckIBUJ-Rwo6QrcxRG9zHoD5U32AZT0wzq5s"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, poster_size = "w342"):
    base_url = "https://image.tmdb.org/t/p"
    return  f"{base_url}/{poster_size}/{poster_api_path}"

def get_movie_info(movies):
    movies_list = []
    for i in movies:
        movies_list.append({"title": i["title"], "poster_path": i["poster_path"]})
    return movies_list

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]