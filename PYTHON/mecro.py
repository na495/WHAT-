import re
from selenium import webdriver

driver = webdriver.Chrome(
    '/Users/nayeon/Documents/VScode_C/PYTHON/chromedriver')  # 웹드라이버 경로 입력
driver_time = webdriver.Chrome(
    '/Users/nayeon/Documents/VScode_C/PYTHON/chromedriver')  # 서버 시간용 웹드라이버 입력

driver_time.get("https://time.navyism.com/?host=www.weverse.io#")
driver.get('https://www.weverse.io/?hl=ko')  # 페이지 열기

checkmsec = driver_time.find_element("id", "msec_check")  # 네이비즘 msec까지 보기
checkmsec.click()  # 네이비즘 msec까지 보기

severtime = driver_time.find_element("id", 'time_area')  # 네이비즘 시-분-초 객체
severmsec = driver_time.find_element("id", 'msec_area')  # 네이비즘 밀리초 객체

while True:
    a = severtime.text  # 네이비즘 시-분-초 가져오기
    b = severmsec.text  # 네이비즘 밀리초 가져오기

    time = re.findall("[0-9]+", a)  # 가져온 시-분-초를 배열하기

    if(time[4] == '33' and time[5] == '59'):  # time[4] : 분, time[5] : 초
        msec = re.findall("[0-9]+", b)  # 가져온 msec 배열하기

        if(int(msec[0]) >= 800):  # msec[0] : 밀리초

            birthday_box = driver.find_element(
                "id", "birthday")  # 생년월일 적을 객체 찾기
            birthday_box.send_keys('20051023')  # 생년월일 적을 객체 찾기

            btn1 = driver.find_element("id", "btn1")
            btn1.click()
            btn2 = driver.find_element("id", "btn2")
            btn2.click()
            btn3 = driver.find_element("id", "btn3")
            btn3.click()

            submit = driver.find_element("id", "done")
            submit.click()

            a = severtime.text
            b = severmsec.text
            print(a + '/' + b)

            break
