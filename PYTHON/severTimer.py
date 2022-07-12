# -*- coding: utf-8 -*-

from datetime import datetime
import urllib.request


month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
         'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

url = 'http://www.naver.com'

severTime = datetime.now()
date = urllib.request.urlopen(url).headers['Date'][5:-4]

sd, sm, sy, shour, smin, ssec = date[:2], month[date[3:6]
                                                ], date[7:11], date[12:14], date[15:17], date[18:]

date_s = (severTime.strftime('%Y년 %m월 %d일 %H시 %M분 %S.%f')[:-3])

print(f'[{url}]의 서버시간\n{sy}년 {sm}월 {sd}일 {shour}시 {smin}분 {ssec}초')
print(date_s)
