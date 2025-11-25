import flask
import limoon
import lxml

content_bp = flask.Blueprint("content", __name__)


@content_bp.route("/basliklar/kanal/<name>")
def channel(name: str) -> str:
    try:
        topics = limoon.get_channel(name)
    except (limoon.ChannelNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("channels.html", channel_name=name, topics=topics)


@content_bp.route("/<path>", methods=["GET", "POST"])
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
        return flask.redirect(flask.url_for("content.topic", path=path, p=page, a="search", day=day, author=author))

    return flask.render_template("topic.html", topic=topic, page=page, action=action)


@content_bp.route("/entry/<int:id>")
def entry(id: int) -> str:
    try:
        entry = limoon.get_entry(id)
    except lxml.etree.ParserError:
        return (
            flask.render_template("not-found.html", description="Empty document received."),
            503,
        )

    return flask.render_template("entry.html", entry=entry)


@content_bp.route("/biri/<nickname>")
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


@content_bp.route("/rozetler/<nickname>")
def author_badges(nickname: str) -> str:
    try:
        badges = limoon.get_author_badges(nickname)
    except (limoon.AuthorNotFound, UnicodeDecodeError) as e:
        return (
            flask.render_template("not-found.html", description=e.__doc__),
            404,
        )

    return flask.render_template("author-badges.html", badges=badges, nickname=nickname)
