from flask import Flask, render_template, url_for, redirect
from flask import request
import tmdb_client as tc
import os
from random import sample, randrange

app=Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('marta_config.cfg', silent=True)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tc.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    list = ["popular", "top_rated", "now_playing", "latest", "upcoming"]
    selected_list = request.args.get('list_type', "popular")
    if selected_list in list:
        movies = tc.get_movies(how_many=8, list_type=selected_list)
        return render_template("homepage.html", movies=movies, current_list=movies, lists=list, active = selected_list)
    else:
        movies = tc.get_movies(how_many=8, list_type="popular")
        return render_template("homepage.html", movies=movies, current_list=movies, lists=list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tc.get_single_movie(movie_id)
    cast = tc.get_single_movie_cast(movie_id)[:4]
    image = tc.get_single_movie_image(movie_id)
    random_image = sample(image, 1)
    image_url = random_image[0]['file_path']
    return render_template("movie_details.html", movie=details, cast=cast, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

