import json
from datetime import datetime, timedelta
from typing import Union

import flask
import limoon
import werkzeug

from .. import configs

utility_bp = flask.Blueprint("utility", __name__)


@utility_bp.route("/external/rentry")
def rentry() -> str:
    try:
        entry = limoon.get_random_entry()
    except (limoon.EntryNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("entry.html", entry=entry)


@utility_bp.route("/external/about")
def about() -> str:
    return flask.render_template("about.html")


@utility_bp.route("/external/privacy-policy")
def privacy_policy() -> str:
    return flask.render_template("privacy-policy.html")


@utility_bp.route("/external/terms-of-service")
def terms_of_service() -> str:
    return flask.render_template("terms-of-service.html")


@utility_bp.route("/external/settings", methods=["GET", "POST"])
def settings() -> Union[str, werkzeug.wrappers.Response]:
    if flask.request.method == "POST":
        action = flask.request.form.get("action", "save")
        response = flask.redirect(flask.url_for("utility.settings"))

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


@utility_bp.route("/rss")
def gundem_xml() -> flask.Response:
    raise NotImplementedError()


@utility_bp.route("/debe/rss")
def debe_xml() -> flask.Response:
    raise NotImplementedError()


@utility_bp.route("/<path>/rss")
def topic_xml(path: str) -> flask.Response:
    raise NotImplementedError()


@utility_bp.route("/robots.txt")
def robots():
    return flask.send_from_directory(utility_bp.static_folder, "robots.txt")


@utility_bp.route("/sitemap.xml")
def sitemap_xml() -> flask.Response:
    static_urls = [
        {"loc": flask.url_for("core.index", _external=True)},
        {"loc": flask.url_for("core.debe", _external=True)},
        {"loc": flask.url_for("core.channels", _external=True)},
        {"loc": flask.url_for("utility.about", _external=True)},
    ]
    channel_urls = [
        {"loc": flask.url_for("content.channel", name=channel.path, _external=True)} for channel in limoon.CHANNELS
    ]

    try:
        agenda_topics = limoon.get_agenda(page=1)
        topic_urls = [
            {"loc": flask.url_for("content.topic", path=topic.path, _external=True)} for topic in agenda_topics
        ]
    except (limoon.AgendaNotFound, UnicodeDecodeError):
        topic_urls = []

    all_urls = static_urls + channel_urls + topic_urls
    response = flask.make_response(flask.render_template("sitemap.xml", all_urls=all_urls))
    response.headers["Content-Type"] = "application/xml"

    return response
