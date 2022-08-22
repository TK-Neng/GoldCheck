import requests
from bs4 import BeautifulSoup
import time

webURL = 'https://www.huasengheng.com/category/review/'
webURL2 = 'https://www.goldtraders.or.th//'
webURL3 = 'https://www.dailyfx.com/gold-price'
r = requests.get(webURL)
r.encoding = 'utf-8'
p = requests.get(webURL2)
p.encoding = 'utf-8'
o = requests.get(webURL3)
o.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
sup = BeautifulSoup(p.text, 'lxml')
sp = BeautifulSoup(o.text, 'lxml')

Linetoken = ''

Lastupdate = " "
Dataupdate = " "
Supplyupdate = " "

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

def DailyfxReport():
    global price
    price = sp.find(class_ = 'dfx-pivotPointsComponent__tableRow dfx-pivotPointsComponent__tableRow--noHover row mx-0 dfx-font-size-3').text


while True:
    GoldPriceCheck()
    HuasenghengReport()
    DailyfxReport()

    if Dataupdate != lblAsTime:
        LineNotifyMessage("ราคาทองตามประกาศของสมาคมค้าทองคำ"+"\n"
        +"ประจำวันที่ "+lblAsTime+"\n"+"ทองคำแท่ง 96.5%\n"+
        "ขายออก "+ lblBLSell+" บาท\n"+"รับซื้อ "+ lblBLBuy+" บาท")
        Dataupdate = lblAsTime

    if Report != Lastupdate :
        LineNotifyMessage("บทวิเคราะห์ใหม่จากHuasenghengมาแล้ว")
        Lastupdate = Report
    
    if price != Supplyupdate :
        LineNotifyMessage("แนวรับแน้วต้านย่อย"+"\n"+price)
        Supplyupdate = price

    time.sleep(60)
    
