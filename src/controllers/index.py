from flask import Flask, render_template, url_for, redirect, request, abort

from src.controllers.forms import Form
from src.models.log import AiAnalysisLog
import settings

app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def get_index():
    form = Form()
    if request.method == 'POST':
        image_path = request.form.get('image_path').strip()
        return render_template('result.html', image_path=image_path)
    return render_template('index.html', form=form)


class WebServer():

    def start(self, debug=False):
        app.config['SECRET_KEY'] = settings.SECRET_KEY
        app.run(host='127.0.0.1', port=settings.PORT, debug=debug)


server = WebServer()