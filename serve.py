#!/usr/bin/python3

from ozgursozluk import app
from ozgursozluk.config import HOST, PORT, DEBUG


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
