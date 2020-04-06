import os
from forms import PhotoUpload
from flask import Flask, render_template, redirect, url_for


IMG_DIR = "static/img/"


class Image:
    def __init__(self, index, filename):
        self.index = index
        self.filename = filename


def image_generator(images):
    for index, filename in enumerate(images):
        yield Image(index, filename)


app = Flask(__name__)


@app.route("/gallery", methods=["GET", "POST"])
def gallery():
    form = PhotoUpload()
    if form.validate_on_submit():
        form.photo.data.save(IMG_DIR + form.photo.data.filename)
    params = {
        "title": "Красная планета",
        "images": list(image_generator(os.listdir(IMG_DIR))),
        "form": form,
    }
    return render_template("gallery.html", **params)


if __name__ == "__main__":
    app.config['SECRET_KEY'] = "SECRET_KEY"
    app.run(port=8080, host="127.0.0.1")
