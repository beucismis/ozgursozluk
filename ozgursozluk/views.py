from flask import url_for, redirect, request, render_template

import ozgursozluk
from ozgursozluk.api import EksiSozluk
from ozgursozluk.utils import last_commit, expires
from ozgursozluk.configs import (
    themes,
    eksi_sozluk_base_urls,
    DEFAULT_THEME,
    DEFAULT_DISPLAY_PINNED_TOPICS,
    DEFAULT_DISPLAY_AUTHOR_NICKNAMES,
    DEFAULT_EKSI_SOZLUK_BASE_URL,
)


es = EksiSozluk()


@ozgursozluk.app.context_processor
def global_template_variables():
    """Return the gloabal template variables."""

    return dict(
        version=ozgursozluk.__version__,
        source=ozgursozluk.__source__,
        description=ozgursozluk.__description__,
        last_commit=last_commit(),
        themes=themes,
        eksi_sozluk_base_urls=eksi_sozluk_base_urls,
    )


@ozgursozluk.app.before_request
def before_request():
    """Set base URL before request."""

    es.base_url = request.cookies.get(
        "eksi_sozluk_base_url", DEFAULT_EKSI_SOZLUK_BASE_URL
    )


@ozgursozluk.app.route("/", methods=["GET", "POST"])
def index():
    """Index route."""

    q = request.args.get("q", default=None, type=str)
    p = request.args.get("p", default=1, type=int)

    if q is not None:
        return redirect(url_for("search", q=q))

    if request.method == "POST":
        return redirect(url_for("search", q=request.form["q"]))

    gundem = es.get_gundem(p)

    return render_template("index.html", gundem=gundem, p=p)


@ozgursozluk.app.route("/<path>")
def topic(path: str):
    """Topic route."""

    p = request.args.get("p", default=1, type=int)
    a = request.args.get("a", default=None, type=str)

    return render_template(
        "topic.html", topic=es.get_topic(path, p, a), p=p, a=a
    )


@ozgursozluk.app.route("/entry/<int:id>")
def entry(id: int):
    """Entry route."""

    return render_template("entry.html", entry=es.get_entry(id))


@ozgursozluk.app.route("/biri/<nickname>")
def author(nickname: str):
    """Author route."""

    return render_template("author.html", author=es.get_author(nickname))


@ozgursozluk.app.route("/debe")
def debe():
    """Debe route."""

    return render_template("debe.html", debe=es.get_debe())


@ozgursozluk.app.route("/search/<q>")
def search(q: str):
    """Search route."""

    return render_template("topic.html", topic=es.search_topic(q), p=1, a=None)


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
            "eksi_sozluk_base_url",
            request.form["eksi_sozluk_base_url"],
            expires=expires(),
        )

        return response

    return render_template(
        "settings.html",
        default_theme=request.cookies.get(
            "theme", DEFAULT_THEME,
        ),
        default_display_pinned_topics=request.cookies.get(
            "display_pinned_topics", DEFAULT_DISPLAY_PINNED_TOPICS,
        ),
        default_display_author_nicknames=request.cookies.get(
            "display_author_nicknames", DEFAULT_DISPLAY_AUTHOR_NICKNAMES,
        ),
        default_eksi_sozluk_base_url=request.cookies.get(
            "eksi_sozluk_base_url", DEFAULT_EKSI_SOZLUK_BASE_URL,
        ),
    )


@ozgursozluk.app.errorhandler(404)
def page_not_found(error):
    """Error handler."""

    return render_template("404.html"), 404
