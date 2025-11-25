import flask
import limoon
import requests

errors_bp = flask.Blueprint("errors", __name__)


@errors_bp.app_errorhandler(404)
def not_found(error) -> tuple[str, int]:
    return flask.render_template("not-found.html", description=error.description), 404


@errors_bp.app_errorhandler(requests.ConnectTimeout)
@errors_bp.app_errorhandler(requests.ConnectionError)
def handle_connection_error(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description="Connection error, please reload page!"),
        503,
    )


@errors_bp.app_errorhandler(limoon.ElementNotFound)
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


@errors_bp.app_errorhandler(limoon.EntryNotFound)
def handle_entry_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.EntryNotFound.__doc__),
        404,
    )


@errors_bp.app_errorhandler(limoon.AuthorNotFound)
def handle_author_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.AuthorNotFound.__doc__),
        404,
    )


@errors_bp.app_errorhandler(limoon.SearchResultNotFound)
def handle_search_result_not_found(error) -> tuple[str, int]:
    return (
        flask.render_template("not-found.html", description=limoon.SearchResultNotFound.__doc__),
        404,
    )
