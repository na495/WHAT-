import re
from selenium import webdriver

driver = webdriver.Chrome(
    '/Users/nayeon/Documents/VScode_C/WHAT-/PYTHON/chromedriver')  # 웹드라이버 경로 입력
driver_time = webdriver.Chrome(
    '/Users/nayeon/Documents/VScode_C/WHAT-/PYTHON/chromedriver')  # 서버 시간용 웹드라이버 입력

driver_time.get("https://time.navyism.com/?host=www.weverse.io#")
driver.get('https://na495.github.io/WHAT-/NULL/NULL.html')  # 페이지 열기

checkmsec = driver_time.find_element("id", "msec_check")  # 네이비즘 msec까지 보기
checkmsec.click()  # 네이비즘 msec까지 보기

severtime = driver_time.find_element("id", 'time_area')  # 네이비즘 시-분-초 객체
severmsec = driver_time.find_element("id", 'msec_area')  # 네이비즘 밀리초 객체

while True:
    a = severtime.text  # 네이비즘 시-분-초 가져오기
    b = severmsec.text  # 네이비즘 밀리초 가져오기

    time = re.findall("[0-9]+", a)  # 가져온 시-분-초를 배열하기

    if(time[4] == '36' and time[5] == '59'):  # time[4] : 분, time[5] : 초
        msec = re.findall("[0-9]+", b)  # 가져온 msec 배열하기

        if(int(msec[0]) >= 950):  # msec[0] : 밀리초
            submit = driver.find_element("id", "done")
            submit.click()
            break
