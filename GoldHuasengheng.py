import requests
from bs4 import BeautifulSoup
import time

webURL = 'https://www.huasengheng.com/category/review/'
r = requests.get(webURL)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')

linetoken = ''

Lastupdate = " "

def LineNotifyMessage(message):
    payload = {'message': message}
    return LineNotify(payload)

def LineNotify(payload,flie=None):
    url = 'https://notify-api.line.me/api/notify'
    token = linetoken
    headers = {'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=headers, data=payload, files=flie)

def HuasenghengReport():
    global Report
    Report = soup.find(id = 'posts-container').text

while True:
    HuasenghengReport()
    if Report != Lastupdate :
        LineNotifyMessage("บทวิเคราะห์ใหม่จากHuasenghengมาแล้ว")
        Lastupdate = Report
    time.sleep(60)
