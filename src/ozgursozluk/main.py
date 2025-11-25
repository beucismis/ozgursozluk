import json
import re
from datetime import UTC, date, datetime

import flask
from limoon.__about__ import __version__ as limoon_version

from . import __version__, configs
from .handlers import errors_bp
from .routes.content import content_bp
from .routes.core import core_bp
from .routes.utility import utility_bp

app = flask.Flask(__name__)
app.secret_key = configs.SECRET_KEY
app.register_blueprint(core_bp)
app.register_blueprint(content_bp)
app.register_blueprint(utility_bp)
app.register_blueprint(errors_bp)


@app.context_processor
def global_variables() -> dict:
    return dict(
        themes=configs.THEMES,
        replaceable_services=configs.REPLACEABLE_SERVICES,
        flask_version=flask.__version__,
        app_version=__version__,
        limoon_version=limoon_version,
        max_date_value=date.today().strftime("%Y-%m-%d"),
    )


@app.template_filter()
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


@app.route("/api/healtcheck")
def healtcheck() -> flask.Response:
    return flask.jsonify(status="healthy", version=__version__, timestamp=datetime.now(UTC))
