from flask import Flask

from ozgursozluk.configs import SECRET_KEY


__version__ = "0.7.2"
__license__ = "WTFPL"
__author__ = "beucismis"
__source__ = "https://github.com/beucismis/ozgursozluk"
__description__ = "a free and open source alternative ekşi sözlük front-end"

app = Flask(__name__)
app.secret_key = SECRET_KEY


import ozgursozluk.views
