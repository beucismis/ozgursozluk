import json
import re
from datetime import date, datetime, timedelta
from typing import NoReturn, Union

import flask
import limoon
import lxml
import requests
import werkzeug
from limoon.__about__ import __version__ as limoon_version

from . import __version__, configs, main


@main.app.context_processor
def global_variables() -> dict:
    return dict(
        themes=configs.THEMES,
        replaceable_services=configs.REPLACEABLE_SERVICES,
        flask_version=flask.__version__,
        app_version=__version__,
        limoon_version=limoon_version,
        max_date_value=date.today().strftime("%Y-%m-%d"),
    )


@main.app.template_filter()
def replace_links(content: str) -> str:
    if flask.request.cookies.get("enable_link_replacements") != "True":
        return content

    replacements_cookie = flask.request.cookies.get("link_replacements", "{}")

    try:
        user_replacements = json.loads(replacements_cookie)
    except json.JSONDecodeError:
        user_replacements = {}

    for service, details in configs.REPLACEABLE_SERVICES.items():
        instance = user_replacements.get(service) or details.get("default_instance")

        if not instance:
            continue

        for original_domain in details["original_domains"]:
            href_pattern = re.compile(
                rf'(<a\s+(?:[^>]*?\s+)?href=["\'])https?://(?:www\.)?{re.escape(original_domain)}',
                re.IGNORECASE,
            )
            content = href_pattern.sub(rf"\1https://{instance}", content)
            text_pattern = re.compile(
                rf"(>https?://(?:www\.)?){re.escape(original_domain)}(?=[/\s<\"'])",
                re.IGNORECASE,
            )
            content = text_pattern.sub(rf"\1{instance}", content)

    return content


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

    try:
        agenda = limoon.get_agenda(page=page)
    except (limoon.AgendaNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("index.html", agenda=agenda, page=page)


@main.app.route("/debe")
def debe() -> str:
    try:
        debe = limoon.get_debe()
    except (limoon.DebeNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("debe.html", debe=debe)


@main.app.route("/kanallar")
def channels() -> str:
    return flask.render_template("channels.html", channels=limoon.CHANNELS)


@main.app.route("/basliklar/kanal/<name>")
def channel(name: str) -> str:
    try:
        topics = limoon.get_channel(name)
    except (limoon.ChannelNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("channels.html", channel_name=name, topics=topics)


@main.app.route("/<path>", methods=["GET", "POST"])
def topic(path: str) -> str:
    page = flask.request.args.get("p", default=1, type=int)
    action = flask.request.args.get("a", default=None, type=str)
    day = flask.request.args.get("day", default=None, type=str)
    author = flask.request.args.get("author", default=None, type=str)

    try:
        topic = limoon.get_topic(path, page=page, action=action, day=day, author=author)
    except (limoon.TopicNotFound, UnicodeDecodeError) as e:
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
    try:
        entry = limoon.get_entry(id)
    except lxml.etree.ParserError:
        return (
            flask.render_template("not-found.html", description="Empty document received."),
            503,
        )

    return flask.render_template("entry.html", entry=entry)


@main.app.errorhandler(limoon.AuthorNotFound)
def handle_author_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.AuthorNotFound.__doc__),
        404,
    )


@main.app.route("/biri/<nickname>")
def author(nickname: str) -> str:
    try:
        author = limoon.get_author(nickname)
        author_last_entrys = limoon.get_author_last_entrys(nickname)
    except (limoon.AuthorNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("author.html", author=author, author_last_entrys=author_last_entrys)


@main.app.route("/rozetler/<nickname>")
def author_badges(nickname: str) -> str:
    try:
        badges = limoon.get_author_badges(nickname)
    except (limoon.AuthorNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

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

    try:
        search_result = limoon.get_search_topic(query)
    except (limoon.SearchResultNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("search.html", search_result=search_result, query=query)


@main.app.route("/external/rentry")
def rentry() -> str:
    try:
        entry = limoon.get_random_entry()
    except (limoon.EntryNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

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
            response.set_cookie("link_replacements", "", expires=0)

            for cookie, default_value in configs.DEFAULT_COOKIES.items():
                response.set_cookie(
                    cookie,
                    default_value,
                    expires=datetime.now() + timedelta(days=365),
                )
            return response

        replacements = {}

        for service, details in configs.REPLACEABLE_SERVICES.items():
            instance = flask.request.form.get(f"replace_{service}")

            if instance:
                replacements[service] = instance

        response.set_cookie(
            "link_replacements",
            json.dumps(replacements),
            expires=datetime.now() + timedelta(days=365),
        )
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
    replacements_cookie = flask.request.cookies.get("link_replacements")
    link_replacements = {}

    if replacements_cookie:
        try:
            link_replacements = json.loads(replacements_cookie)
        except json.JSONDecodeError:
            pass

    return flask.render_template(
        "settings.html",
        selected_theme=cookies.pop("theme"),
        link_replacements=link_replacements,
        **cookies,
    )


@main.app.route("/rss")
def gundem_xml() -> flask.Response:
    raise NotImplementedError()


@main.app.route("/debe/rss")
def debe_xml() -> flask.Response:
    raise NotImplementedError()


@main.app.route("/<path>/rss")
def topic_xml(path: str) -> flask.Response:
    raise NotImplementedError()


@main.app.errorhandler(404)
def not_found(error) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=error.description), 404
