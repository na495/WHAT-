import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "/Users/nayeon/Documents/VScode_C/WHAT-/PYTHON/chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver_time = webdriver.Chrome(
    '/Users/nayeon/Documents/VScode_C/WHAT-/PYTHON/chromedriver')  # 서버 시간용 웹드라이버 입력

# 위버스 페이지 열기
driver.get('https://na495.github.io/WHAT-/')
# 네이비즘 페이지 열기
driver_time.get("https://time.navyism.com/?host=www.weverse.io#")

checkmsec = driver_time.find_element(
    By.ID, 'msec_check')  # 네이비즘 msec까지 보기 버튼 찾기
checkmsec.click()  # 네이비즘 msec까지 보기 클릭

severtime = driver_time.find_element(By.ID, 'time_area')  # 네이비즘 시-분-초 객체
severmsec = driver_time.find_element(By.ID, 'msec_area')  # 네이비즘 밀리초 객체

link = driver.find_element(
    By.CLASS_NAME, 'NULL')  # 참여 신청 클릭, 폼으로 이동
link.click()

while True:
    a = severtime.text  # 네이비즘 시-분-초 가져오기
    b = severmsec.text  # 네이비즘 밀리초 가져오기

    time = re.findall("[0-9]+", a)  # 가져온 시-분-초를 배열하기

    if(time[4] == '37' and time[5] == '19'):  # time[4] : 분, time[5] : 초
        msec = re.findall("[0-9]+", b)  # 가져온 msec 배열하기

        if(int(msec[0]) >= 900):  # msec[0] : 밀리초

            birthday_box = driver.find_element(
                By.ID, 'requiredProperties-birthDate')  # 생년월일 적을 객체 찾기
            birthday_box.send_keys('20051023')  # 생년월일 적기

            btn1 = driver.find_element(By.NAME, 'terms-8744')  # 동의 버튼1 클릭
            btn1.click()
            btn2 = driver.find_element(By.NAME, 'terms-8745')  # 동의 버튼2 클릭
            btn2.click()
            btn3 = driver.find_element(By.NAME, 'terms-8746')  # 동의 버튼3 클릭
            btn3.click()

            submit = driver.find_element(By.CLASS_NAME, 'bVoNaW')  # 제출 버튼 클릭
            submit.click()

            a = severtime.text
            b = severmsec.text
            print(a + '/' + b)

            break
