from requests import get, post, put, delete

from Robot import Path, headers, simpleObj
from Robot.http import HTTP_OK

URL = Path + '/maps/'


def POST(post_maps):
    """
    Add a new map to the robot
    :param post_maps: The details of the maps
    :return: GetMaps
    """
    return GetMaps(
        post(URL, headers=headers, json=post_maps.json())
    )


def GET():
    """
    Retrieve the list of maps from the robot
    :return: < GetMaps > array
    """
    return GetMaps_objects_array(
        get(URL, headers=headers)
    )


def GET_guid(guid):
    """
    Retrieve the details about the map with the specified GUID
    :param guid: The guid to search for, string
    :return: GetMap
    """
    return GetMap(
        get(URL + guid, headers=headers)
    )


def PUT(guid, put_map):
    """
    Modify the values of the map with the specified GUID
    :param guid: PutMap
    :return: GetMap
    """
    return GetMap(
        put(URL + guid, headers=headers, json=put_map.json())
    )


def DELETE(guid):
    delete(
        URL + guid, headers=headers
    )


class GetMaps:
    def __init__(self, request):
        self.status_code = request.status_code
        self.json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK

    def name(self):
        return self.json['name']

    def guid(self):
        return self.json['guid']


class GetMap:
    def __init__(self, request):
        self.status_code = request.status_code
        self.json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK

    def created_by(self):
        return self.json['created_by']

    def created_by_id(self):
        return self.json['created_by_id']

    def guid(self):
        return self.json['guid']

    def map(self):
        return self.json['map']

    def metadata(self):
        return self.json['metadata']

    def name(self):
        return self.json['name']

    def origin_theta(self):
        return self.json['origin_theta']

    def origin_x(self):
        return self.json['origin_x']

    def origin_y(self):
        return self.json['origin_y']

    def path_guides(self):
        return self.json['path_guides']

    def paths(self):
        return self.json['paths']

    def positions(self):
        return self.json['positions']

    def resolution(self):
        return self.json['resolution']

    def session_id(self):
        return self.json['session_id']


class GetMaps_objects_array:
    def __init__(self, request):
        self.status_code = request.status_code
        self.json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK

    def json(self):
        return [simpleObj(j) for j in self.json()]


class PostMaps:
    def __init__(self, map, metadata, name, origin_theta, origin_x, origin_y, resolution, session_id):
        self._body = {
            'created_by_id': None,
            'guid': None,
            'map': map,
            'metadata': metadata,
            'name': name,
            'origin_theta': origin_theta,
            'origin_x': origin_x,
            'origin_y': origin_y,
            'resolution': resolution,
            'session_id': session_id
        }

    def created_by_id(self, created_by_id):
        self._body['created_by_id'] = created_by_id
        return self

    def guid(self, guid):
        self._body['guid'] = guid
        return self

    def json(self):
        return self._body


class PutMap:
    def __init__(self):
        self._body = {}

    def map(self, map):
        self._body['map'] = map
        return self

    def metadata(self, metadata):
        self._body['metadata'] = metadata
        return self

    def name(self, name):
        self._body['name'] = name
        return self

    def origin_theta(self, origin_theta):
        self._body['origin_theta'] = origin_theta
        return self

    def origin_x(self, origin_x):
        self._body['origin_x'] = origin_x
        return self

    def origin_y(self, origin_y):
        self._body['origin_y'] = origin_y
        return self

    def resolution(self, resolution):
        self._body['resolution'] = resolution
        return self

    def json(self):
        return self._body
