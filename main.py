from flask import Flask, render_template, url_for, redirect
from flask import request
import tmdb_client as tc
import os

app=Flask(__name__)


@app.route('/')
def homepage():
    movies= tc.get_popular_movies()
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)

