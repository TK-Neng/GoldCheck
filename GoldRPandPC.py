import requests
from bs4 import BeautifulSoup
import time

webURL = 'https://www.huasengheng.com/category/review/'
webURL2 = 'https://www.goldtraders.or.th//'
r = requests.get(webURL)
r.encoding = 'utf-8'
p = requests.get(webURL2)
p.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
sup = BeautifulSoup(p.text, 'lxml')

Linetoken = 'bsvOIVbilEBaJ60ZERWH2MK3NKrgUCFlV9W7iikER37'

Lastupdate = " "
Dataupdate = " "

def LineNotifyMessage(message):
    payload = {'message': message}
    return LineNotify(payload)

def LineNotify(payload,flie=None):
    url = 'https://notify-api.line.me/api/notify'
    token = Linetoken
    headers = {'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=headers, data=payload, files=flie)

def HuasenghengReport():
    global Report
    Report = soup.find(id = 'posts-container').text

def GoldPriceCheck():
    global lblAsTime,lblBLSell,lblBLBuy
    lblAsTime = sup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text
    lblBLSell = sup.find(id = 'DetailPlace_uc_goldprices1_lblBLSell').text
    lblBLBuy = sup.find(id = 'DetailPlace_uc_goldprices1_lblBLBuy').text


while True:
    HuasenghengReport()
    GoldPriceCheck()
    if Report != Lastupdate :
        LineNotifyMessage("บทวิเคราะห์ใหม่จากHuasenghengมาแล้ว")
        Lastupdate = Report
    if Dataupdate != lblAsTime:
        LineNotifyMessage("ราคาทองตามประกาศของสมาคมค้าทองคำ"+"\n"
        +"ประจำวันที่ "+lblAsTime+"\n"+"ทองคำแท่ง 96.5%\n"+
        "ขายออก "+ lblBLSell+" บาท\n"+"รับซื้อ "+ lblBLBuy+" บาท")
        Dataupdate = lblAsTime
    time.sleep(60)
    