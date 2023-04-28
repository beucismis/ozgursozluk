from datetime import datetime, timedelta

from flask import url_for, redirect, request, render_template

import ozgursozluk
from ozgursozluk.api import Eksi
from ozgursozluk.config import (
    DEFAULT_THEME,
    DEFAULT_DISPLAY_AUTHOR_NICKNAME,
    DEFAULT_EKSI_BASE_URL,
)


eksi = Eksi()


def _last_commit() -> str:
    with open(".git/refs/heads/main") as file:
        return file.read()


def _expires() -> datetime:
    return datetime.now() + timedelta(days=365)


@ozgursozluk.app.context_processor
def context_processor():
    return dict(
        version=ozgursozluk.__version__,
        source=ozgursozluk.__source__,
        description=ozgursozluk.__description__,
        last_commit=_last_commit(),
    )


@ozgursozluk.app.route("/", methods=["GET", "POST"])
def index():
    q = request.args.get("q", default=None, type=str)
    p = request.args.get("p", default=1, type=int)

    if q is not None:
        return redirect(url_for("search", q=q))

    if request.method == "POST":
        return redirect(url_for("search", q=request.form["q"]))

    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)
    gundem = eksi.get_gundem(p)

    return render_template("index.html", gundem=gundem, p=p)


@ozgursozluk.app.route("/search/<q>")
def search(q: str):
    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return render_template("topic.html", topic=eksi.search_topic(q), p=1, a=None)


@ozgursozluk.app.route("/<title>")
def topic(title: str):
    p = request.args.get("p", default=1, type=int)
    a = request.args.get("a", default=None, type=str)
    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return render_template(
        "topic.html", topic=eksi.get_topic(title, p, a), p=p, a=a
    )


@ozgursozluk.app.route("/debe")
def debe():
    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return render_template("debe.html", debe=eksi.get_debe())


@ozgursozluk.app.route("/entry/<int:id>")
def entry(id: int):
    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return render_template("topic.html", topic=eksi.get_entry(id), p=1)


@ozgursozluk.app.route("/biri/<nickname>")
def author(nickname: str):
    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return render_template("author.html", author=eksi.get_author(nickname))


@ozgursozluk.app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        response = redirect(url_for("settings"))
        response.set_cookie(
            "theme",
            request.form["theme"],
            expires=_expires(),
        )
        response.set_cookie(
            "display_author_nickname",
            request.form["display_author_nickname"],
            expires=_expires(),
        )
        response.set_cookie(
            "eksi_base_url",
            request.form["eksi_base_url"],
            expires=_expires(),
        )

        return response

    return render_template(
        "settings.html",
        theme=request.cookies.get(
            "theme", DEFAULT_THEME
        ),
        display_author_nickname=request.cookies.get(
            "display_author_nickname", DEFAULT_DISPLAY_AUTHOR_NICKNAME
        ),
        eksi_base_url=request.cookies.get(
            "eksi_base_url", DEFAULT_EKSI_BASE_URL
        ),
    )


@ozgursozluk.app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error), 404
