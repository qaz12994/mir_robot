from requests import get, post, put, delete

from Robot import Path, headers, simpleObj
from Robot.http import HTTP_OK, HTTP_Created

URL = Path + '/sessions/'


def POST(post_sessions):
    """
    Add a new session to the robot
    :param post_sessions: PostSessions
    :return: GetSessions
    """
    return GetSessions(
        post(URL, headers=headers, json=post_sessions.json())
    )


def GET():
    """
    Retrieve the list of sessions from the robot
    :return: <GetSessions> array
    """
    return GetSession_objects_array(
        get(URL, headers=headers)
    )


def GET_guid(guid):
    """
    Retrieve the details about the session with the specified GUID
    :param guid: The guid to search for
    :return: GetSessions
    """
    return GetSessions(
        get(URL + guid, headers=headers)
    )


def PUT(guid, put_session):
    """
    Modify the values of the session with the specified GUID
    :param guid: The guid to modify
    :param put_session: PutSession
    :return: GetSession
    """
    return GetSessions(
        put(URL + guid, headers=headers, json=put_session.json())
    )


def DELETE(guid):
    """
    Erase the session with the specified GUID
    :param guid: The guid to delete
    :return: No Content
    """
    delete(URL + guid, headers=headers)


def GET_sessionID_maps(session_id):
    """
    Retrieve the list of maps that belong to the session with the specified session ID
    :param session_id: The session_id to search for
    :return: < GetSession_maps > array
    """
    return GetSession_objects_array(
        get(URL + session_id + '/maps', headers=headers)
    )


def GET_sessionID_missions(session_id):
    """
    Retrieve the list of missions that belong to the session with the specified session ID
    :param session_id: The session_id to search for
    :return:< GetSession_missions > array
    """
    return GetSession_objects_array(
        get(URL + session_id + '/missions', headers=headers)
    )


class GetSessions:
    def __init__(self, request):
        self.status_code = request.status_code
        self._json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK or \
               self.status_code == HTTP_Created

    def name(self):
        return self._json['name']

    def guid(self):
        return self._json['guid']


class GetSession_objects_array:
    def __init__(self, request):
        self.status_code = request.status_code
        self._json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK or \
               self.status_code == HTTP_Created

    def array(self):
        return [simpleObj(j) for j in self._json]


class PostSessions:
    def __init__(self, name):
        self._body = {
            'created_by_id': None,
            'description': None,
            'guid': None,
            'name': name
        }

    def created_by_id(self, created_by_id):
        self._body['created_by_id'] = created_by_id
        return self

    def description(self, description):
        self._body['description'] = description
        return self

    def guid(self, guid):
        self._body['guid'] = guid
        return self

    def json(self):
        return self._body


class PutSession:
    def __init__(self):
        self._body = {}

    def description(self, description):
        self._body['description'] = description
        return self

    def name(self, name):
        self._body['name'] = name
        return self

    def value(self, value):
        self._body['value'] = value
        return self

    def json(self):
        return self._body
