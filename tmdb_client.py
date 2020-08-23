import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzA4MDM3OGY5OTBhMTRhY2ZlZGFhOWYzNGJhM2I2NiIsInN1YiI6IjVmMmZhMmYxM2MzYWIwMDAzNDQ5NzdhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wtiKJS3SckIBUJ-Rwo6QrcxRG9zHoD5U32AZT0wzq5s"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()