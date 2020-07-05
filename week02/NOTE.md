学习笔记
反爬虫
一：浏览器的头部解决反爬虫
1、解决user-agent 的问题
1、带http的头部信息
   a: user-agent 的模拟 :
fake-useragent
使用 from fake-useragent import UserAgent   导入库
ua = UserAgent(verify_ssl=False) (#添加参数的目的是不去验证IP，防止被
封掉)
#模拟不同的浏览器
print(f'Chrome:'ua.chrome)

#随机的浏览器
print(f'随机浏览器：{ua.random}')
注意：尽量模拟不同的浏览器进行请求

user-agent 的存放：在requests 是在 user-agent
如果是scrapy 中则在settings.py 中设置

2、user-agent 和 referer和 host  一般做个补全 来解决

2、解决cookies 的问题
1、直接复制，但是大项目的时候不适用，cookies 有个有效期的问题
   所以一般不推荐使用。
2、模拟用户的登录：
浏览器的获取方法：
post  方法
response = requests.post('//post',data={'key':'vaule'})
response.json() 
和cookies 的使用

3、post 填充邮箱和密码
   post 放入到scrapy 中的 start_url 


发起请求的用
requests.Session()


3、模拟浏览器的点击行为 WebDriver 
      1、安装 selenium 
            from selenium import webdriver

