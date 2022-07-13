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
driver.get('https://www.weverse.io/enhypen/notices/2991')
# 네이비즘 페이지 열기
driver_time.get("https://time.navyism.com/?host=www.weverse.io#")

checkmsec = driver_time.find_element(
    By.ID, 'msec_check')  # 네이비즘 msec까지 보기 버튼 찾기
checkmsec.click()  # 네이비즘 msec까지 보기 클릭

severtime = driver_time.find_element(By.ID, 'time_area')  # 네이비즘 시-분-초 객체
severmsec = driver_time.find_element(By.ID, 'msec_area')  # 네이비즘 밀리초 객체


while True:
    a = severtime.text  # 네이비즘 시-분-초 가져오기
    b = severmsec.text  # 네이비즘 밀리초 가져오기

    time = re.findall("[0-9]+", a)  # 가져온 시-분-초를 배열하기

    if(time[4] == '59' and time[5] == '59'):  # time[4] : 분, time[5] : 초
        msec = re.findall("[0-9]+", b)  # 가져온 msec 배열하기

        if(int(msec[0]) >= 950):  # msec[0] : 밀리초
            submit = driver.find_element(By.CLASS_NAME, 'bVoNaW')
            submit.click()

            a = severtime.text
            b = severmsec.text
            print(a, b)  # 네이비즘 시-분-초 출력
            break
