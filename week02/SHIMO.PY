from selenium import webdriver
import time

try:
    browser_ch = webdriver.Chrome()
    browser_ch.get('https://shimo.im/welcome')
    time.sleep(5)
#找到对应的按钮，然后点击
    find_tm = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    find_tm.click()

#往里面填写用户名以及密码
    browser_ch.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')\
        .send_keys('18392538857')
    time.sleep(3)
    browser_ch.find_chelement_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')\
        .send_keys('FLH838300')
    time.sleep(3)
    browser_ch.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    print('登录成功')
    time.sleep(3)
except Exception as everay_error:
    print(everay_error)
