from flask import Flask, render_template, url_for, redirect, request, abort

import settings

app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER)


@app.route('/', methods=["GET", "POST"])
def get_index():
    return render_template('index.html')


class WebServer():
    def start(self, debug=False):
        app.run(host="127.0.0.1", port=settings.PORT, debug=debug)


server = WebServer()