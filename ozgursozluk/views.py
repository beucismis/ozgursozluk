from random import randint

from flask import url_for, redirect, request, render_template

import ozgursozluk
from ozgursozluk.scraper import EksiSozluk
from ozgursozluk.utils import last_commit, expires, contributors
from ozgursozluk.configs import THEMES, DEFAULT_COOKIES


es = EksiSozluk()


@ozgursozluk.app.context_processor
def global_template_variables():
    """Return the gloabal template variables."""

    return dict(
        themes=THEMES,
        last_commit=last_commit(),
        contributors=contributors(),
        version=ozgursozluk.__version__,
        source_code=ozgursozluk.__source_code__,
        description=ozgursozluk.__description__,
    )


@ozgursozluk.app.route("/", methods=["GET", "POST"])
def index():
    """Index route."""

    q = request.args.get("q", default=None, type=str)
    p = request.args.get("p", default=1, type=int)

    if q is not None:
        return redirect(url_for("search", q=q))

    if request.method == "POST":
        return redirect(url_for("search", q=request.form["q"] or None))

    gundem = es.get_gundem(p)

    return render_template("index.html", gundem=gundem, p=p)


@ozgursozluk.app.route("/<path>")
def topic(path: str):
    """Topic route."""

    p = request.args.get("p", default=1, type=int)
    a = request.args.get("a", default=None, type=str)

    return render_template("topic.html", topic=es.get_topic(path, p, a), p=p, a=a)


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


@ozgursozluk.app.route("/search")
def search():
    """Search route."""

    q = request.args.get("q", default=None, type=str)

    if q is None or not bool(len(q)):
        return render_template("404.html"), 404

    return render_template("search.html", search_result=es.search_topic(q), q=q)


@ozgursozluk.app.route("/random")
def random():
    """Random entry route."""

    return redirect(url_for("entry", id=randint(1, 300_000_000)))


@ozgursozluk.app.route("/donate")
def donate():
    """Donate route."""

    return render_template("donate.html")


@ozgursozluk.app.route("/settings", methods=["GET", "POST"])
def settings():
    """Settings route."""

    if request.method == "POST":
        response = redirect(url_for("settings"))

        for cookie in DEFAULT_COOKIES:
            response.set_cookie(cookie, request.form[cookie], expires=expires())

        return response

    return render_template(
        "settings.html",
        # Unpack DEFAULT_COOKIES variable to the template
        **{
            f"default_{cookie}": request.cookies.get(cookie, DEFAULT_COOKIES[cookie])
            for cookie in DEFAULT_COOKIES
        },
    )


@ozgursozluk.app.errorhandler(404)
def page_not_found(error):
    """Error handler route."""

    return render_template("404.html"), 404
