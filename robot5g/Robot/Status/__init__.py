from requests import get, put

from Robot import Path, headers
from Robot.http import HTTP_OK

URL = Path + '/status/'


def GET():
    """
    Retrieve the status of the robot
    :return: GetStatus
    """
    return GetStatus(
        get(URL)
    )


def PUT(put_status: 'PutStatus'):
    """
    Modify the status of the robot
    :param put_status: PutStatus
    :return: GetStatus
    """
    return GetStatus(
        put(URL, headers=headers, json=put_status.json())
    )


class GetStatus:
    def __init__(self, request):
        self.status_code = request.status_code
        self.json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK

    def position(self):
        position = self.json['position']
        return position['y'], position['x']

    def orientation(self):
        return self.json['position']['orientation']

    def state_id(self):
        return self.json['state_id']

    def state_text(self):
        return self.json['state_text']

    def session_id(self):
        return self.json['session_id']


class PutStatus:
    def __init__(self):
        self._body = {}

    def answer(self, answer):
        self._body['answer'] = answer
        return self

    def clear_error(self, clear_error):
        self._body['clear_error'] = clear_error
        return self

    def datetime(self, datetime):
        self._body['datetime'] = datetime
        return self

    def guid(self, guid):
        self._body['guid'] = guid
        return self

    def map_id(self, map_id):
        self._body['map_id'] = map_id
        return self

    def mode_id(self, mode_id):
        self._body['mode_id'] = mode_id
        return self

    def name(self, name):
        self._body['name'] = name
        return self

    def serial_number(self, serial_number):
        self._body['serial_number'] = serial_number
        return self

    def state_id(self, state_id):
        self._body['state_id'] = state_id
        return self

    def json(self):
        return self._body
