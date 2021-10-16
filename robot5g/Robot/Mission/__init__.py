from requests import get, post, put, delete

from Robot import Path, headers, simpleObj
from Robot.http import HTTP_OK, HTTP_Created, HTTP_NoContent

URL = Path + '/missions/'


def POST(body: 'PostMissions') -> 'GetMissions':
    """
    Add a new mission to the robot
    :param body: PostMissions
    :return:GetMissions
    """
    return GetMissions(
        post(URL, headers=headers, json=body.json())
    )


def GET() -> 'GetMission_objects_array':
    """
    Retrieve the list of missions in the robot
    :return:<GetMissions> array
    """
    return GetMission_objects_array(
        get(URL, headers=headers)
    )


def GET_guid(guid: str) -> 'GetMissions':
    """
    Retrieve the details about the mission with the specified GUID
    :param guid: The guid to search for
    :return: GetMissions
    """
    return GetMissions(
        get(URL + guid, headers=headers)
    )


def PUT(guid: str, body: 'PutMission'):
    """
    Modify the values of the mission with the specified GUID
    :param guid: The guid to modify
    :param body: PutMission
    :return: GetMission
    """
    return GetMissions(
        put(URL + guid, headers=headers, json=body.json())
    )


def DELETE(guid: str) -> bool:
    """
    Erase the mission with the specified GUID
    :param guid:  The guid to delete
    :return: No Content
    """
    return delete(URL + guid, headers=headers).status_code == HTTP_NoContent


def POST_missionID_actions(mission_id: str, body: 'PostMission_actions'):
    """
    Add a new action to the mission with the specified mission ID
    :param body: <PostMission_actions>
    :param mission_id: mission id
    :return: <GetMission_actions>
    """
    return GetMission_actions(
        post(URL + mission_id + '/actions', headers=headers, json=body.json())
    )


def GET_missionID_actions(mission_id: str) -> 'GetMission_actions':
    """
    Retrieve the list of actions that belong to the mission with the specified mission ID
    :param mission_id: The mission_id to search for
    :return:<GetMission_actions> array
    """
    return GetMission_actions(
        get(URL + mission_id + '/actions', headers=headers)
    )


def GET_missionID_actionID(mission_id: str, action_id: str):
    """
    Retrieve the details about the action with the specified GUID that belongs to the mission with the specified mission ID
    :param mission_id: The mission_id to search for
    :param action_id: The action_id to search for
    :return: <GetMission_action>
    """
    return GetMission_action(
        get(f'{URL}{mission_id}/actions/{action_id}', headers=headers)
    )


def PUT_missionID_actionID(mission_id, action_id):
    """

    Modify the values of the action with the specified GUID that belongs to the mission with the specified mission ID
    :param mission_id: The mission_id to search for <PutMission_action>
    :param action_id: The action_id to search for
    :return:<GetMission_action>
    """
    return GetMission_action(
        put(URL + mission_id + '/actions' + action_id, headers=headers)
    )


def DELETE_missionID_actionID(mission_id, action_id):
    """
    Erase the action with the specified GUID from the mission with the specified mission ID
    :param mission_id: The mission_id to search for
    :param action_id: The action_id to search for
    :return: No Content
    """
    return delete(URL + mission_id + '/actions' + action_id, headers=headers).status_code == HTTP_NoContent


class GetMission_objects_array:
    def __init__(self, request):
        self.status_code = request.status_code
        self._json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK or \
               self.status_code == HTTP_Created

    def array(self):
        return [simpleObj(j) for j in self._json]


class GetMissions:
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


class PostMissions:
    def __init__(self, group_id: str, name: str):
        self._body = {
            'group_id': group_id,
            'name': name,
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

    def hidden(self, hidden):
        self._body['hidden'] = hidden
        return self

    def session_id(self, session_id):
        self._body['session_id'] = session_id
        return self

    def json(self):
        return self._body


class PutMission:
    def __init__(self):
        self._body = {}

    def description(self, description):
        self._body['description'] = description
        return self

    def group_id(self, group_id):
        self._body['group_id'] = group_id
        return self

    def hidden(self, hidden):
        self._body['hidden'] = hidden
        return self

    def name(self, name):
        self._body['name'] = name
        return self

    def session_id(self, session_id):
        self._body['hidden'] = session_id
        return self

    def json(self):
        return self._body


class GetMission_actions:
    def __init__(self, request):
        self.status_code = request.status_code
        self._json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK or \
               self.status_code == HTTP_Created

    def action_type(self):
        return self._json['action_type']

    def guid(self):
        return self._json['guid']

    def mission_id(self):
        return self._json['mission_id']

    def parameters(self):
        return self._json['parameters']

    def priority(self):
        return self._json['priority']


class PostMission_actions:
    def __init__(self, action_type, parameters, priority=1):
        self._body = {
            'action_type': action_type,
            'parameters': parameters,
            'priority': priority,
        }

    def guid(self, guid):
        self._body['guid'] = guid
        return self

    def mission_id(self, mission_id):
        self._body['mission_id'] = mission_id
        return self

    def scope_reference(self, scope_reference):
        self._body['scope_reference'] = scope_reference
        return self

    def json(self):
        return self._body


class GetMission_action:
    def __init__(self, request):
        self.status_code = request.status_code
        self._json = request.json()

    def Success(self):
        return self.status_code == HTTP_OK or \
               self.status_code == HTTP_Created

    def action_type(self):
        return self._json['action_type']

    def guid(self):
        return self._json['guid']

    def mission_id(self):
        return self._json['mission_id']

    def parameters(self):
        return self._json['parameters']

    def priority(self):
        return self._json['priority']

    def scope_reference(self):
        return self._json['scope_reference']


class PutMission_action:
    def __init__(self):
        self._body = {}

    def parameters(self, parameters):
        self._body['parameters'] = parameters
        return self

    def priority(self, priority):
        self._body['priority'] = priority
        return self

    def scope_reference(self, scope_reference):
        self._body['scope_reference'] = scope_reference
        return self

    def json(self):
        return self._body
