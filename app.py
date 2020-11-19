"""Package & module import."""
from flask import Flask, render_template, url_for
from generator.dictionary_words import make_sentence

app = Flask(__name__)


@app.route("/")
def sentence():
    """Return random generated sentence."""
    sentence = make_sentence("mimsys-joke.txt")
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    app.run(debug=True)
