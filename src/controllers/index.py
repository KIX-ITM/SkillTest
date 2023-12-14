from flask import Flask, render_template, url_for, redirect, request, abort

from src.controllers.forms import Form
from src.models.log import AiAnalysisLog
from src.controllers import lib
import settings

app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def get_index():
    # image_path入力画面
    # image_pathをPOSTした場合はAPI結果を表示
    form = Form()
    if request.method == 'POST':
        image_path = request.form.get('image_path').strip()
        response = lib.post_example_api(image_path)
        if 'error' in response:
            return render_template('result.html', log_data=None, error=response['error'])
        else:
            log_data = lib.create_log_data(
                image_path,
                response['response_data'],
                response['request_timestamp'],
                response['response_timestamp']
            )
            record = AiAnalysisLog.create(log_data)
            record_dict = record.__dict__
            print(record_dict)
            return render_template('result.html', record=record_dict, error=None)
    return render_template('index.html', form=form)


class WebServer():

    def start(self, debug=False):
        # テスト用サーバー設定
        app.config['SECRET_KEY'] = settings.SECRET_KEY
        app.run(host='127.0.0.1', port=settings.PORT, debug=debug)


server = WebServer()