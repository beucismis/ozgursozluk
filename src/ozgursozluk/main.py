from datetime import datetime, UTC

import flask

from . import __version__, configs


app = flask.Flask(__name__)
app.secret_key = configs.SECRET_KEY


@app.route("/api/healtcheck")
def healtcheck() -> flask.Response:
    return flask.jsonify(status="healthy", version=__version__, timestamp=datetime.now(UTC))


@app.route("/external/privacy-policy")
def privacy_policy() -> str:
    return flask.render_template("privacy-policy.html")


@app.route("/external/terms-of-service")
def terms_of_service() -> str:
    return flask.render_template("terms-of-service.html")


from . import views
