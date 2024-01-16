#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("0-hello_route")


@app.route("/airbnb-onepage/")
def hello_hbnb():
    """Return a given string"""
    return "<h1 style='color:blue'>Hello HBNB!</h1>"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
