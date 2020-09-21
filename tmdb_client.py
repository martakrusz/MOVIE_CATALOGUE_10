import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzA4MDM3OGY5OTBhMTRhY2ZlZGFhOWYzNGJhM2I2NiIsInN1YiI6IjVmMmZhMmYxM2MzYWIwMDAzNDQ5NzdhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wtiKJS3SckIBUJ-Rwo6QrcxRG9zHoD5U32AZT0wzq5s"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_poster_url(poster_api_path, poster_size = "w342"):
    base_url = "https://image.tmdb.org/t/p"
    return  f"{base_url}/{poster_size}/{poster_api_path}"

def get_movie_info(movies):
    movies_list = []
    for i in movies:
        movies_list.append({"title": i["title"], "poster_path": i["poster_path"]})
    return movies_list

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    response =  call_tmdb_api(f"movie/{movie_id}/credits")
    return response["cast"]

def get_single_movie_image(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")