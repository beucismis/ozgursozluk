from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from typing import NoReturn, Union

import flask
import limoon
import requests
import werkzeug
from limoon.__about__ import __version__ as limoon_version

from . import __version__, configs, main


@main.app.context_processor
def global_variables() -> dict:
    return dict(
        themes=configs.THEMES,
        flask_version=flask.__version__,
        app_version=__version__,
        limoon_version=limoon_version,
        max_date_value=date.today().strftime("%Y-%m-%d"),
    )


@main.app.errorhandler(requests.ConnectTimeout)
@main.app.errorhandler(requests.ConnectionError)
def handle_connection_error(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description="Connection error, please reload page!"),
        503,
    )


@main.app.errorhandler(limoon.ElementNotFound)
def handle_element_error(error) -> tuple[str, int]:
    return (
        flask.render_template(
            "not-found.html",
            description=error.__doc__,
            message=error.message,
            html=error.html,
        ),
        503,
    )


@main.app.route("/", methods=["GET", "POST"])
def index() -> Union[str, werkzeug.wrappers.Response]:
    query = flask.request.args.get("q", default=None, type=str)
    page = flask.request.args.get("p", default=1, type=int)

    if query is not None:
        return flask.redirect(flask.url_for("search", q=query))

    if flask.request.method == "POST":
        return flask.redirect(flask.url_for("search", q=flask.request.form["q"] or None))

    agenda = limoon.get_agenda(page=page)

    return flask.render_template("index.html", agenda=agenda, page=page)


@main.app.route("/debe")
def debe() -> str:
    debe = limoon.get_debe()

    return flask.render_template("debe.html", debe=debe)


@main.app.route("/kanallar")
def channels() -> str:
    return flask.render_template("channels.html", channels=limoon.CHANNELS)


@main.app.route("/basliklar/kanal/<name>")
def channel(name: str) -> str:
    topics = limoon.get_channel(name)

    return flask.render_template("channels.html", channel_name=name, topics=topics)


@main.app.route("/<path>", methods=["GET", "POST"])
def topic(path: str) -> str:
    page = flask.request.args.get("p", default=1, type=int)
    action = flask.request.args.get("a", default=None, type=str)
    day = flask.request.args.get("day", default=None, type=str)
    author = flask.request.args.get("author", default=None, type=str)

    try:
        topic = limoon.get_topic(path, page=page, action=action, day=day, author=author)
    except limoon.TopicNotFound as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    if flask.request.method == "POST":
        author = flask.request.form.get("author", None)
        day = flask.request.form.get("day", None)
        return flask.redirect(flask.url_for("topic", path=path, p=page, a="search", day=day, author=author))

    return flask.render_template("topic.html", topic=topic, page=page, action=action)


@main.app.errorhandler(limoon.EntryNotFound)
def handle_entry_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.EntryNotFound.__doc__),
        404,
    )


@main.app.route("/entry/<int:id>")
def entry(id: int) -> str:
    entry = limoon.get_entry(id)

    return flask.render_template("entry.html", entry=entry)


@main.app.errorhandler(limoon.AuthorNotFound)
def handle_author_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.AuthorNotFound.__doc__),
        404,
    )


@main.app.route("/biri/<nickname>")
def author(nickname: str) -> str:
    author = limoon.get_author(nickname)
    author_last_entrys = limoon.get_author_last_entrys(nickname)

    return flask.render_template("author.html", author=author, author_last_entrys=author_last_entrys)


@main.app.route("/rozetler/<nickname>")
def author_badges(nickname: str) -> str:
    badges = limoon.get_author_badges(nickname)

    return flask.render_template("author-badges.html", badges=badges, nickname=nickname)


@main.app.errorhandler(limoon.SearchResultNotFound)
def handle_search_result_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.SearchResultNotFound.__doc__),
        404,
    )


@main.app.route("/search")
def search() -> Union[str, NoReturn]:
    query = flask.request.args.get("q", default=None, type=str)

    if not query:
        return flask.abort(404, description=limoon.SearchResultNotFound.__doc__)

    search_result = limoon.get_search_topic(query)

    return flask.render_template("search.html", search_result=search_result, query=query)


@main.app.route("/external/rentry")
def rentry() -> str:
    entry = limoon.get_random_entry()

    return flask.render_template("entry.html", entry=entry)


@main.app.route("/external/about")
def about() -> str:
    return flask.render_template("about.html")


@main.app.route("/external/settings", methods=["GET", "POST"])
def settings() -> Union[str, werkzeug.wrappers.Response]:
    if flask.request.method == "POST":
        action = flask.request.form.get("action", "save")
        response = flask.redirect(flask.url_for("settings"))

        if action == "reset":
            response.set_cookie(
                "theme",
                configs.DEFAULT_THEME,
                expires=datetime.now() + timedelta(days=365),
            )
            for cookie, default_value in configs.DEFAULT_COOKIES.items():
                if cookie != "theme":
                    response.set_cookie(
                        cookie,
                        default_value,
                        expires=datetime.now() + timedelta(days=365),
                    )
            return response

        theme = flask.request.form.get("theme", configs.DEFAULT_THEME)

        if theme not in configs.THEMES:
            theme = configs.DEFAULT_THEME

        response.set_cookie("theme", theme, expires=datetime.now() + timedelta(days=365))

        for cookie in configs.DEFAULT_COOKIES:
            if cookie != "theme":
                value = "True" if flask.request.form.get(cookie) else "False"
                response.set_cookie(cookie, value, expires=datetime.now() + timedelta(days=365))

        return response

    cookies = {
        cookie: flask.request.cookies.get(cookie, default_value)
        for cookie, default_value in configs.DEFAULT_COOKIES.items()
    }

    return flask.render_template("settings.html", selected_theme=cookies.pop("theme"), **cookies)


@main.app.route("/rss")
def gundem_xml() -> flask.Response:
    agenda = limoon.get_agenda(page=1)
    agenda = [topic for topic in agenda if topic.path]

    with ThreadPoolExecutor() as executor:
        topics = list(executor.map(limoon.get_topic, [topic.path for topic in agenda]))

    response = flask.make_response(flask.render_template("gundem.xml", topics=topics))
    response.headers["Content-Type"] = "application/xml"

    return response


@main.app.route("/debe/rss")
def debe_xml() -> flask.Response:
    debe = limoon.get_debe()
    debe = [entry for entry in debe if entry.id]
    response = flask.make_response(flask.render_template("debe.xml", debe=debe))
    response.headers["Content-Type"] = "application/xml"

    return response


@main.app.route("/<path>/rss")
def topic_xml(path: str) -> flask.Response:
    page = flask.request.args.get("p", default=1, type=int)
    action = flask.request.args.get("a", default=None, type=str)
    author = flask.request.args.get("author", default=None, type=str)
    topic = limoon.get_topic(path, page=page, action=action, author=author)
    response = flask.make_response(flask.render_template("topic.xml", topic=topic))
    response.headers["Content-Type"] = "application/xml"

    return response


@main.app.errorhandler(404)
def not_found(error) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=error.description), 404
