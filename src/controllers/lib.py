from datetime import datetime
import random

from src.api import example_api
import settings


def create_log_data(image_path, response_data, request_timestamp, response_timestamp):
    estimated_data = response_data['estimated_data']
    img_class = estimated_data['class'] if 'class' in estimated_data else None
    confidence = estimated_data['confidence'] if 'confidence' in estimated_data else None
    new_data = dict(
        image_path=image_path,
        success=response_data['success'],
        message=response_data['message'],
        img_class=img_class,
        confidence=confidence,
        request_timestamp=request_timestamp,
        response_timestamp=response_timestamp
    )
    return new_data


def post_example_api(image_path):
    str_image_path = str(image_path)
    request_timestamp = datetime.now()
    response = example_api.post(str_image_path)
    if 'error' in response:
        return dict(error=response['error'])
    else:
        response_timestamp = request_timestamp + response.elapsed
        response_data = get_response_data(response)
        return dict(
            response_timestamp=response_timestamp,
            response_data=response_data,
            request_timestamp=request_timestamp
        )


def get_response_data(response):
    if settings.TEST:
        response_data = format_response_data(get_random_dummy_json_data())
    else:
        response_data = format_response_data(response.json())
    return response_data


def format_response_data(response_json):
    data = dict(
        success=response_json['success'],
        message=response_json['message'],
        estimated_data=response_json['estimated_data']
    )
    return data


def get_random_dummy_json_data():
    json_data_list = [
        settings.DUMMY_SUCCESS_RESPONSE_JSON,
        settings.DUMMY_FAILURE_RESPONSE_JSON
    ]
    return random.choice(json_data_list)