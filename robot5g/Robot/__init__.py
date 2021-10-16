Address = 'http://mir.com'
# Address = 'http://192.168.1.79'
Host = Address + '/api'
BasePath = '/v2.0.0'
Path = Host + BasePath
# header，API有規範
headers = {
    'Content-Type': 'application/json',
    'Accept-Language': 'en_US',
    'Authorization': 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='
}


# 因為有許多回傳直都長一樣(guid, name, name)，所以建立一個統一的回傳物件
class simpleObj:
    def __init__(self, object):
        self._guid = object['guid']
        self._name = object['name']
        self._url = object['name']

    def guid(self):
        return self._guid

    def name(self):
        return self._name

    def url(self):
        return self._url
"""
API中
Function對應各個Restful API網址
物件的用法則是
1. 解析回傳物件:Getter，Function call完的回傳值是物件，用物件中的Function取得各個值
2. 建立傳送body:Post、PUT，會需要body，先建立好body後再放入Function call
   body的建立：若是必要參數，會用建構子；反之，會用Builder Pattern去建立(.各個Function去新增)
   Node.MissionPoster.py有example
"""