import os

from flask import Blueprint, request as flask_request, make_response
import requests

main = Blueprint('main', __name__, url_prefix='/main')


@main.route('/test', methods=['POST'])
def test():
    port = os.environ['FLOWER_PORT']
    user_password = os.environ['FLOWER_BASIC_AUTH']
    base = os.environ['FLOWER_HOST']
    url = f"http://{user_password}@{base}:{port}/api/task/async-apply/"

    test_request_param = flask_request.json
    delay = test_request_param.get('delay')

    params = {"args": (delay, "auto")}
    resp = requests.post(os.path.join(url, 'queue_1:task_type_1'), json=params)
    print(resp.status_code)

    res = make_response(resp.text)
    res.mimetype = 'json'

    return res
