# -*- coding: utf-8 -*-
import schedule
import time
import urllib.request


month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
         'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

url = 'https://www.naver.com/'

i = 0


def TTT():
    for i in range(1, 201, 1):
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        sd, sm, sy, shour, smin, ssec = date[:2], month[date[3:6]
                                                        ], date[7:11], date[12:14], date[15:17], date[18:]

        print(f'{i}. 네이버의 서버 시간은 {sy}년 {sm}월 {sd}일 {shour}시 {smin}분 {ssec}초')


schedule.every().day.at("14:15:00").do(TTT)

while True:
    schedule.run_pending()
