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
    movies = tc.get_popular_movies()["results"][:8]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)

