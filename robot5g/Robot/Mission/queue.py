import requests

from Robot import Path, headers

URL = Path + '/mission_queue/'


def GET():
    return requests.get(URL)


def GET_ID(ID):
    return requests.get(URL + ID)


def POST(mission_id, priority=1):
    json = {
        'mission_id': mission_id,
        'priority': priority
    }
    return requests.post(url=URL,
                         headers=headers,
                         json=json)


def DELETE():
    return requests.delete(URL, headers=headers)


def isEmpty():
    return True
