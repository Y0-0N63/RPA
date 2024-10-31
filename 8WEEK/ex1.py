# Web Crawling -> Web Page로부터 데이터를 가져오는 것이 목적
# 1. 조작 시나리오 확인
# 2. Selenium 코드의 역할
# 2-1. 접속할 사이트 지정
# 2-2. 페이지 내에서 데이터 접근 or 검색 실행 코드
# + 검색 실행이란 -> 페이지 내 엘리먼트를 조작하는 것
# ㄴ 엘리먼트 찾기 -> 마우스, 키 입력

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 2-1
url = 'https://www.google.co.kr/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# 2-2
search_box = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
search_box.send_keys("KBO 한국시리즈")
# 엔터키 입력 코드
search_box.send_keys(Keys.RETURN)
time.sleep(20)