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
