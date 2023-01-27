import requests
from bs4 import BeautifulSoup
import datetime

nowTime = str(datetime.datetime.now())
# print(nowTime)
day=nowTime[:4]+nowTime[5:7]+nowTime[8:10]
# print(day)
req = requests.get("https://school.cbe.go.kr/chungjuja-e/M01040504/list?ymd=20230109")
#print(req.text)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup)

atag = soup.find("a", href="/chungjuja-e/M01040504/list?ymd=20230109")
#print(atag)
li = atag.find_all('li')
#print(li)

foodKind = ""

for i in li:
    foodKind = foodKind + i.text + "\n"

# print(foodKind)

import telegram
토큰 = "5623859694:AAFppcQ94lZkQBn-ry7qGBa6jw0_v8Rn3ac"
봇 = telegram.Bot(token = 토큰)
# for i in 봇.getUpdates():
#     print(i.message)
봇.send_message(5623859694, foodKind)