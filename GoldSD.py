import requests
from bs4 import BeautifulSoup
import time


webURL = 'https://www.dailyfx.com/gold-price'
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

def DailyfxReport():
    global price
    price = soup.find(class_ = 'dfx-pivotPointsComponent__tableRow dfx-pivotPointsComponent__tableRow--noHover row mx-0 dfx-font-size-3').text


while True:
    DailyfxReport()
    print(price)
    if price != Lastupdate :
        LineNotifyMessage("แนวรับแน้วต้านย่อย"+"\n"+price)
        Lastupdate = price
    
    time.sleep(5)
