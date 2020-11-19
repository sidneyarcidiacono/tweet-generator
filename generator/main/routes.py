"""Package & module import."""
from flask import Blueprint, render_template
from generator.dictionary_words import make_sentence

main = Blueprint("main", __name__)


@main.route("/")
def sentence():
    """Return random generated sentence."""
    sentence = make_sentence("mimsys-joke.txt")
    return render_template("index.html", sentence=sentence)


@main.route("/tweet")
def tweet():
    pass
