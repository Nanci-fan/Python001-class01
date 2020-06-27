#使用requests 获取maoyan TOP100 的电影
#使用beatuifulsoup

import requests
from bs4 import BeautifulSoup as bs 

##设置浏览器头部
user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl ='https://maoyan.com/board/4'

response = requests.get(myurl,headers = header)

print(response.text)
print(f'返回码是：{response.status_code}')

#使用beatuifulsoup 获得网页信息和链接
bs_info = bs(response.text,'html.parser')
for tags in bs_info.find_all('div',attrs={'class':'movie-item-info'}):
    for ptag in tags.find_all('p',attrs={'class':'name'}):
        for atag in ptag.find_all('a',):
            #a_href = atag.get('href')

            print(atag.get('href'))

            print(atag.get('title'))


