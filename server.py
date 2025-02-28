# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
# ]
# ///
from flask import Flask, request, render_template
from catalogue import Catalogue

app = Flask(__name__)


@app.get("/")
def home():
    catalogue = (
        Catalogue()
        .filter(request.args.getlist("filter"))
        .search(request.args.get("search"))
        .sort(request.args.get("sort"))
    )
    if request.headers.get("Accept") == "application/json":
        return catalogue.films
    else:
        return render_template(
            "index.html",
            films=catalogue.films,
            directors=catalogue.directors,
        )


if __name__ == "__main__":
    Flask.run(app)
