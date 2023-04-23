import flask

import ozgursozluk
from ozgursozluk.api import Eksi
from ozgursozluk.config import DEFAULT_THEME, DEFAULT_EKSI_BASE_URL


eksi = Eksi()


@ozgursozluk.app.context_processor
def context_processor():
    return dict(
        version=ozgursozluk.__version__,
        source=ozgursozluk.__source__,
        description=ozgursozluk.__description__,
    )


@ozgursozluk.app.route("/", methods=["GET", "POST"])
def index():
    q = flask.request.args.get("q", default=None, type=str)

    if q is not None:
        return flask.redirect(flask.url_for("search", q=q))

    if flask.request.method == "POST":
        return flask.redirect(flask.url_for("search", q=flask.request.form["q"]))

    eksi.base_url = flask.request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)
    agenda = eksi.get_agenda()

    return flask.render_template("index.html", agenda=agenda)


@ozgursozluk.app.route("/search/<q>")
def search(q: str):
    eksi.base_url = flask.request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return flask.render_template("topic.html", topic=eksi.search_topic(q), p=1)


@ozgursozluk.app.route("/<title>")
def topic(title: str):
    p = flask.request.args.get("p", default=1, type=int)
    eksi.base_url = flask.request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)
    result = eksi.get_topic(title, p)

    return flask.render_template("topic.html", topic=result, p=p)


@ozgursozluk.app.route("/entry/<int:id>")
def entry(id: int):
    eksi.base_url = flask.request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    return flask.render_template("topic.html", topic=eksi.get_entry(id), p=1)


@ozgursozluk.app.route("/settings", methods=["GET", "POST"])
def settings():
    theme = flask.request.cookies.get("theme", DEFAULT_THEME)
    eksi_base_url = flask.request.cookies.get("eksi_base_url", DEFAULT_EKSI_BASE_URL)

    if flask.request.method == "POST":
        response = flask.make_response(
            flask.render_template(
                "settings.html", theme=theme, eksi_base_url=eksi_base_url
            )
        )
        response.set_cookie("theme", flask.request.form["theme"])
        response.set_cookie("eksi_base_url", flask.request.form["eksi_base_url"])

        return response

    return flask.render_template(
        "settings.html", theme=theme, eksi_base_url=eksi_base_url
    )


@ozgursozluk.app.errorhandler(404)
def page_not_found(e):
    return flask.render_template("404.html"), 404
