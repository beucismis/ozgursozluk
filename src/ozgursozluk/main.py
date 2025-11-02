from datetime import UTC, datetime

import flask

from . import __version__, configs

app = flask.Flask(__name__)
app.secret_key = configs.SECRET_KEY


@app.route("/robots.txt")
def robots():
    return flask.send_from_directory(app.static_folder, "robots.txt")


@app.route("/external/privacy-policy")
def privacy_policy() -> str:
    return flask.render_template("privacy-policy.html")


@app.route("/external/terms-of-service")
def terms_of_service() -> str:
    return flask.render_template("terms-of-service.html")


@app.route("/api/healtcheck")
def healtcheck() -> flask.Response:
    return flask.jsonify(status="healthy", version=__version__, timestamp=datetime.now(UTC))


from . import views
