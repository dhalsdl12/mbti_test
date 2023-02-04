from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time
import os


driver = webdriver.Chrome()

f = open("mbti.txt", 'r', encoding="utf-8")
check = ''
for i in range(48):
    line = f.readline()
    if i % 3 == 0:
        tmp = line.split(' ')
        check = tmp[0]
        try:
            if not os.path.exists(check):
                os.makedirs(check)
            else:
                print(check + '이미 존재합니다.')
        except OSError:
            pass
        continue
    tmp = line.split(',')
    for name in tmp:
        name = name.strip()
        
        driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
        elem = driver.find_element(By.NAME, 'q')
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)

        images = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')
        for img in range(20):
            try:
                images[img].click()
                time.sleep(1)
                imgURL = driver.find_element(By.CSS_SELECTOR, '.n3VNCb').get_attribute('src')
                urllib.request.urlretrieve(imgURL, check + '/' + name + str(img) + '.jpg')
            except:
                pass
driver.close()
f.close()

'''elem = driver.find_element(By.NAME, 'q')
elem.send_keys('권오민')
elem.send_keys(Keys.RETURN)

images = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')
count = 0
os.mkdir("download")
for img in images:
    try:
        count += 1
        if count > 30:
            break
        img.click()
        time.sleep(1)
        imgURL = driver.find_element(By.CSS_SELECTOR, '.n3VNCb').get_attribute('src')
        urllib.request.urlretrieve(imgURL, './download/' + str(count) + '.jpg')
    except:
        pass'''
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()