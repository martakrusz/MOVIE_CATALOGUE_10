import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzA4MDM3OGY5OTBhMTRhY2ZlZGFhOWYzNGJhM2I2NiIsInN1YiI6IjVmMmZhMmYxM2MzYWIwMDAzNDQ5NzdhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wtiKJS3SckIBUJ-Rwo6QrcxRG9zHoD5U32AZT0wzq5s"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_url, poster_size = "w342"):
    base_url = "https://image.tmdb.org/t/p"
    return  f"{base_url}/{poster_size}/{poster_url}"