"""
取得機器人位置
並貼到剪貼簿
"""
import requests
import win32clipboard as wc


# Get robot position and modify to clipboard
if __name__ == '__main__':
    r = requests.get('http://mir.com/api/v2.0.0/status')
    wc.OpenClipboard()
    if r.status_code == 200:
        position = r.json()['position']
        wc.SetClipboardData(wc.CF_UNICODETEXT, str(position['x']) + ' ' + str(position['y']))
    else:
        wc.SetClipboardData(wc.CF_UNICODETEXT, 'ERROR')
    wc.CloseClipboard()

