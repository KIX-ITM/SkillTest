from datetime import datetime

import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout

import settings


def post(image_path):
    # API実行
    url = settings.API_URL
    data = {
        'image_path': image_path,
    }
    # ステータスコード200番台以外はエラーハンドリング
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except ConnectionError as ce:
        return create_error_response("Connection Error:", ce)
    except HTTPError as he:
        return create_error_response("HTTP Error:", he)
    except Timeout as te:
        return create_error_response("Timeout Error:", te)
    except RequestException as re:
        return create_error_response("Error:", re)
    return response


def create_error_response(error_name, detail):
    # エラー時のレスポンス内容を作成
    error_text = f'{error_name} {detail}'
    return dict(error=error_text)
