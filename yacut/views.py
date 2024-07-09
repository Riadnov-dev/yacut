import random

from flask import render_template, flash, redirect, url_for

from yacut import app, db
from .constants import SHORT_ID_LENGTH, CHARACTERS
from .forms import UrlMapForm
from .models import URLMap


def get_unique_short_id(length=SHORT_ID_LENGTH):
    while True:
        short_id = "".join(random.choices(CHARACTERS, k=length))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id


@app.route("/", methods=["GET", "POST"])
def index():
    form = UrlMapForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data or get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash("Предложенный вариант короткой ссылки уже существует.",
                  "error"
                  )
        else:
            url_map = URLMap(original=original_link, short=custom_id)
            db.session.add(url_map)
            db.session.commit()
            short_link = url_for(
                "redirect_to_original",
                short_id=custom_id, _external=True
            )
            flash(f"Короткая ссылка создана: {short_link}", "success")
            return render_template("index.html",
                                   form=form,
                                   short_link=short_link
                                   )

    return render_template("index.html", form=form)


@app.route("/<short_id>")
def redirect_to_original(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
