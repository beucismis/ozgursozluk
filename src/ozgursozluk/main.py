import flask

from . import configs


app = flask.Flask(__name__)
app.secret_key = configs.SECRET_KEY


from . import views
