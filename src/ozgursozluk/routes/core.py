from typing import NoReturn, Union

import flask
import limoon
import werkzeug

core_bp = flask.Blueprint("core", __name__)


@core_bp.route("/", methods=["GET", "POST"])
def index() -> Union[str, werkzeug.wrappers.Response]:
    query = flask.request.args.get("q", default=None, type=str)
    page = flask.request.args.get("p", default=1, type=int)

    if query is not None:
        return flask.redirect(flask.url_for("core.search", q=query))

    if flask.request.method == "POST":
        return flask.redirect(flask.url_for("core.search", q=flask.request.form["q"] or None))

    try:
        agenda = limoon.get_agenda(page=page)
    except (limoon.AgendaNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("index.html", agenda=agenda, page=page)


@core_bp.route("/debe")
def debe() -> str:
    try:
        debe = limoon.get_debe()
    except (limoon.DebeNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("debe.html", debe=debe)


@core_bp.route("/kanallar")
def channels() -> str:
    return flask.render_template("channels.html", channels=limoon.CHANNELS)


@core_bp.route("/search")
def search() -> Union[str, NoReturn]:
    query = flask.request.args.get("q", default=None, type=str)

    if not query:
        return flask.abort(404, description=limoon.SearchResultNotFound.__doc__)

    try:
        search_result = limoon.get_search_topic(query)
    except (limoon.SearchResultNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("search.html", search_result=search_result, query=query)
