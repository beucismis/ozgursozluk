from flask import Flask


__version__ = "0.4.3"
__author__ = "beucismis"
__source__ = "https://github.com/beucismis/ozgursozluk"
__description__ = "a free and open source alternative ekşi sözlük front-end"

app = Flask(__name__)
app.config.from_object("ozgursozluk.config")


import ozgursozluk.views
