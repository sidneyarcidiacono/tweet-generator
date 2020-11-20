"""Package & module import."""
from flask import Blueprint, render_template, request
from generator.sample import select, hist, weighted_sample_helper

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def sentence():
    """Return random generated sentence."""
    if request.method == "POST":
        length = int(request.form.get("length"))
        sample = select(hist, weighted_sample_helper(hist), length)
        return render_template("index.html", sentence=sample)
    return render_template("index.html")


@main.route("/add-favorite/<sentence>", methods=["POST"])
def add_favorite(sentence):
    """Add sentence to favorites when user clicks like button."""
    pass


@main.route("/favorites")
def favorites():
    """Show favorited sentences to users."""

    # TODO: include logic to query all favorited
    # sentences from database, pass to template
    pass
