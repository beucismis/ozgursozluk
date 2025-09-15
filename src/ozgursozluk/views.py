import random
from datetime import datetime, timedelta
from typing import NoReturn, Union

import flask
import limoon
import requests
from limoon.__about__ import __version__ as limoon_version

from . import __version__, configs, main


@main.app.context_processor
def global_template_variables() -> dict:
    return dict(
        themes=configs.THEMES,
        flask_version=flask.__version__,
        app_version=__version__,
        limoon_version=limoon_version,
    )


@main.app.errorhandler(requests.ConnectTimeout)
@main.app.errorhandler(requests.ConnectionError)
def handle_index_not_found(e) -> tuple[str, int]:
    return flask.render_template("not-found.html", description="API connection error, please reload page!"), 404


@main.app.route("/", methods=["GET", "POST"])
def index() -> Union[str, flask.Response]:
    q = flask.request.args.get("q", default=None, type=str)
    p = flask.request.args.get("p", default=1, type=int)

    if q is not None:
        return flask.redirect(flask.url_for("search", q=q))

    if flask.request.method == "POST":
        return flask.redirect(flask.url_for("search", q=flask.request.form["q"] or None))

    agenda = limoon.get_agenda()

    return flask.render_template("index.html", agenda=agenda, p=p)


@main.app.route("/debe")
def debe() -> str:
    debe = limoon.get_debe()

    return flask.render_template("debe.html", debe=debe)


@main.app.route("/<path>")
def topic(path: str) -> str:
    p = flask.request.args.get("p", default=1, type=int)
    a = flask.request.args.get("a", default=None, type=str)
    topic = limoon.get_topic(path, p)

    return flask.render_template("topic.html", topic=topic, p=p, a=a)


@main.app.errorhandler(limoon.EntryNotFound)
def handle_entry_not_found(e) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=limoon.EntryNotFound.__doc__), 404


@main.app.route("/entry/<int:id>")
def entry(id: int) -> str:
    entry = limoon.get_entry(id)

    return flask.render_template("entry.html", entry=entry)


@main.app.errorhandler(AttributeError)
def handle_author_not_found(e) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=limoon.AuthorNotFound.__doc__), 404


@main.app.route("/biri/<nickname>")
def author(nickname: str) -> str:
    author = limoon.get_author(nickname)
    author_last_entrys = limoon.get_author_last_entrys(nickname)

    return flask.render_template("author.html", author=author, author_last_entrys=author_last_entrys)


@main.app.errorhandler(AttributeError)
def handle_search_result_not_found(e) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=limoon.SearchResultNotFound.__doc__), 404


@main.app.route("/search")
def search() -> Union[str, NoReturn]:
    q = flask.request.args.get("q", default=None, type=str)

    if q is None or not bool(len(q)):
        return flask.abort(404, description=limoon.SearchResultNotFound.__doc__)

    search_result = limoon.get_search_topic(q)

    return flask.render_template("search.html", search_result=search_result, q=q)


@main.app.route("/rentry")
def rentry() -> flask.Response:
    return flask.redirect(flask.url_for("entry", id=random.randint(1, 300_000_000)))


@main.app.route("/about")
def about() -> str:
    return flask.render_template("about.html")


@main.app.route("/settings", methods=["GET", "POST"])
def settings() -> Union[str, flask.Response]:
    if flask.request.method == "POST":
        response = flask.redirect(flask.url_for("settings"))

        for cookie in configs.DEFAULT_COOKIES:
            if cookie == "theme":
                value = flask.request.form.get("theme", configs.DEFAULT_THEME)
            else:
                if flask.request.form.get(cookie) is not None:
                    value = "True"
                else:
                    value = "False"

            response.set_cookie(cookie, value, expires=datetime.now() + timedelta(days=365))

        return response

    return flask.render_template(
        "settings.html",
        selected_theme=flask.request.cookies.get("theme", configs.DEFAULT_THEME),
        **{
            cookie: flask.request.cookies.get(cookie, configs.DEFAULT_COOKIES[cookie])
            for cookie in configs.DEFAULT_COOKIES
        },
    )


@main.app.errorhandler(404)
def not_found(error) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=error.description), 404
