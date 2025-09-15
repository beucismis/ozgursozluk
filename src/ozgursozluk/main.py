from datetime import datetime, UTC

import flask

from . import __version__, configs


app = flask.Flask(__name__)
app.secret_key = configs.SECRET_KEY


@app.route("/healtcheck")
def healtcheck() -> flask.Response:
    return flask.jsonify(status="healthy", version=__version__, timestamp=datetime.now(UTC))


@app.route("/privacy-policy")
def privacy_policy() -> str:
    return flask.render_template("privacy-policy.html")


@app.route("/terms-of-service")
def terms_of_service() -> str:
    return flask.render_template("terms-of-service.html")


from . import views
