"""Package & module import."""
from flask import Blueprint, render_template, request, redirect, url_for
from generator.sample import select, hist, weighted_sample_helper
from generator import db

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def sentence():
    """Return random generated sentence."""
    if request.method == "POST":
        length = int(request.form.get("length"))
        sample = select(hist, weighted_sample_helper(hist), length)
        return render_template("index.html", sentence=sample)
    return render_template("index.html")


@main.route("/add-favorite", methods=["POST"])
def add_favorite():
    """Add sentence to favorites when user clicks like button."""
    favorite_sentence = request.form.get("sentence")
    new_fav = {"sentence": favorite_sentence}
    db.favorites.insert_one(new_fav)
    return redirect(url_for("main.sentence"))


@main.route("/favorites")
def favorites():
    """Show favorited sentences to users."""
    favorites = list(db.favorites.find())
    context = {"favorites": favorites}
    return render_template("favorites.html", **context)
