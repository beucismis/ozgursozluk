from flask import url_for, redirect, request, render_template

import ozgursozluk
from ozgursozluk.api import Eksi
from ozgursozluk.utils import last_commit, expires
from ozgursozluk.config import (
    DEFAULT_THEME,
    DEFAULT_DISPLAY_PINNED_TOPICS,
    DEFAULT_DISPLAY_AUTHOR_NICKNAMES,
    DEFAULT_EKSI_BASE_URL,
)


eksi = Eksi()


@ozgursozluk.app.context_processor
def global_template_variables():
    """Return the gloabal template variables."""

    return dict(
        version=ozgursozluk.__version__,
        source=ozgursozluk.__source__,
        description=ozgursozluk.__description__,
        last_commit=last_commit(),
    )


@ozgursozluk.app.before_request
def before_request():
    """Set base URL before request."""

    eksi.base_url = request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)


@ozgursozluk.app.route("/", methods=["GET", "POST"])
def index():
    """Index route."""

    q = request.args.get("q", default=None, type=str)
    p = request.args.get("p", default=1, type=int)

    if q is not None:
        return redirect(url_for("search", q=q))

    if request.method == "POST":
        return redirect(url_for("search", q=request.form["q"]))

    gundem = eksi.get_gundem(p)

    return render_template("index.html", gundem=gundem, p=p)


@ozgursozluk.app.route("/<path>")
def topic(path: str):
    """Topic route."""

    p = request.args.get("p", default=1, type=int)
    a = request.args.get("a", default=None, type=str)

    return render_template(
        "topic.html", topic=eksi.get_topic(path, p, a), p=p, a=a
    )


@ozgursozluk.app.route("/entry/<int:id>")
def entry(id: int):
    """Entry route."""

    return render_template("entry.html", entry=eksi.get_entry(id))


@ozgursozluk.app.route("/biri/<nickname>")
def author(nickname: str):
    """Author route."""

    return render_template("author.html", author=eksi.get_author(nickname))


@ozgursozluk.app.route("/debe")
def debe():
    """Debe route."""

    return render_template("debe.html", debe=eksi.get_debe())


@ozgursozluk.app.route("/search/<q>")
def search(q: str):
    """Search route."""

    return render_template("topic.html", topic=eksi.search_topic(q), p=1, a=None)


@ozgursozluk.app.route("/settings", methods=["GET", "POST"])
def settings():
    """Settings route."""

    if request.method == "POST":
        response = redirect(url_for("settings"))
        response.set_cookie(
            "theme",
            request.form["theme"],
            expires=expires(),
        )
        response.set_cookie(
            "display_pinned_topics",
            request.form["display_pinned_topics"],
            expires=expires(),
        )
        response.set_cookie(
            "display_author_nicknames",
            request.form["display_author_nicknames"],
            expires=expires(),
        )
        response.set_cookie(
            "eksi_base_url",
            request.form["eksi_base_url"],
            expires=expires(),
        )

        return response

    return render_template(
        "settings.html",
        theme=request.cookies.get(
            "theme", DEFAULT_THEME,
        ),
        display_pinned_topics=request.cookies.get(
            "display_pinned_topics", DEFAULT_DISPLAY_PINNED_TOPICS,
        ),
        display_author_nicknames=request.cookies.get(
            "display_author_nicknames", DEFAULT_DISPLAY_AUTHOR_NICKNAMES,
        ),
        eksi_base_url=request.cookies.get(
            "eksi_base_url", DEFAULT_EKSI_BASE_URL,
        ),
    )


@ozgursozluk.app.errorhandler(404)
def page_not_found(error):
    """Error handler."""

    return render_template("404.html"), 404
