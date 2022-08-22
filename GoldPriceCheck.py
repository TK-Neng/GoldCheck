import requests
from bs4 import BeautifulSoup
import time

webURL = 'https://www.goldtraders.or.th/'
r = requests.get(webURL)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')

Linetoken = ''

Lastupdate = " "

def LineNotifyMessage(message):
    payload = {'message': message}
    return LineNotify(payload)

def LineNotify(payload,flie=None):
    url = 'https://notify-api.line.me/api/notify'
    token = Linetoken
    headers = {'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=headers, data=payload, files=flie)

def GoldPriceCheck():
    # print("ราคาทองตามประกาศของสมาคมค้าทองคำ")
    # print("ประจำวันที่ "+soup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text)
    # print("ทองคำแท่ง 96.5%")
    # print("ขายออก "+ soup.find(id = 'DetailPlace_uc_goldprices1_lblBLSell').text+" บาท")
    # print("รับซื้อ "+ soup.find(id = 'DetailPlace_uc_goldprices1_lblBLBuy').text+" บาท")

    # LineNotifyMessage("ราคาทองตามประกาศของสมาคมค้าทองคำ")
    # LineNotifyMessage("ประจำวันที่ "+soup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text)
    # LineNotifyMessage("ทองคำแท่ง 96.5%")
    # LineNotifyMessage("ขายออก "+ soup.find(id = 'DetailPlace_uc_goldprices1_lblBLSell').text+" บาท")
    # LineNotifyMessage("รับซื้อ "+ soup.find(id = 'DetailPlace_uc_goldprices1_lblBLBuy').text+" บาท")
    
    global lblAsTime,lblBLSell,lblBLBuy
    lblAsTime = soup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text
    lblBLSell = soup.find(id = 'DetailPlace_uc_goldprices1_lblBLSell').text
    lblBLBuy = soup.find(id = 'DetailPlace_uc_goldprices1_lblBLBuy').text

while True:
    GoldPriceCheck()
    print(" ")
    print("ราคาทองตามประกาศของสมาคมค้าทองคำ")
    print("ประจำวันที่ "+lblAsTime)
    print("ทองคำแท่ง 96.5%")
    print("ขายออก "+ lblBLSell+" บาท")
    print("รับซื้อ "+ lblBLBuy+" บาท")

    if Lastupdate != lblAsTime:
        LineNotifyMessage("ราคาทองตามประกาศของสมาคมค้าทองคำ"+"\n"
        +"ประจำวันที่ "+lblAsTime+"\n"+"ทองคำแท่ง 96.5%\n"+
        "ขายออก "+ lblBLSell+" บาท\n"+"รับซื้อ "+ lblBLBuy+" บาท")
        Lastupdate = lblAsTime

    time.sleep(60)
