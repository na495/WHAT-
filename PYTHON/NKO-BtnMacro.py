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
driver.get('https://www.weverse.io/seventeen/notice/2962')
# 네이비즘 페이지 열기
driver_time.get("http://nko.kr/?url=https%3A%2F%2Fwww.weverse.io%2F")


severtime = driver_time.find_element(
    By.ID, 'nkoclockdisplay')

submit = driver.find_element(By.CLASS_NAME, 'bVoNaW')  # 제출 버튼

while True:
    a = severtime.text  # 네이비즘 시-분-초 가져오기
    time = re.findall("[0-9]+", a)  # 가져온 시-분-초를 배열하기

    if(time[1] == '50' and time[2] == '59'):  # time[4] : 분, time[5] : 초
        if(int(time[3]) >= 800):  # msec[0] : 밀리초
            submit.click()

            a = severtime.text
            print(a)  # 네이비즘 시-분-초 출력
            break
