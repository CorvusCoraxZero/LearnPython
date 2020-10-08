'''
url一般由三个部分组成
    第一部分是协议：http, https, ftp, file, ed2k.....
    第二部分是存放资源的服务器的域名系统或者IP地址（有时还需加上端口号）
    第三部分是资源的具体地址，如目录或者文件名等'''
"""
Pyrton可以通过urllib这个包 访问互联网
    urllib包中有四个模块，分别是，urllib.request  urllib.error  urllib.parse  urllib.robotparser
    
"""
import urllib.request as ulrequest

# response = ulrequest.urlopen("http://www.fishc.com")
# html = response.read()
# print(html)
# print(html.decode("utf-8")) #将网页的二进制数据转化为正常的形式
# req = ulrequest.Request("http://placekitten.com/900/561")
# response = ulrequest.urlopen(req) #这里也可以用Request对象来访问
# print(response.geturl())
# print(response.info())
# print(response.getcode())
#
# """实战 爬取一只猫"""
# response = ulrequest.urlopen("http://placekitten.com/900/561")
# cat_img = response.read()
# with open("cat_900_561.jpg",'wb') as f:
#     f.write(cat_img)
# print("保存图片成功")

"""实战 利用有道词典来翻译文本"""
import urllib.request
import urllib.parse
import json
import time

while True:

    content = input("请输入你要翻译的内容(输入'Q!'退出程序)：")
    if content == 'Q!':
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    #修改heads模拟正常的浏览器访问 方法1
    '''head = {}
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    '''
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16018840684524'
    data['sign'] = '7c001b5d1e96aa03e60b5e154c5e3d24'
    data['lts'] = '1601884068452'
    data['bv'] = 'bc3c53120c4167be4925b7d40ff2fd56'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode("utf8")

    head={} #修改heads模拟正常的浏览器访问 方法2
    req = urllib.request.Request(url, data ,head)
    #修改heads模拟正常的浏览器访问 方法2
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")

    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    target = json.loads(html) #将html这个json的数据转换为字典的格式 以便取出其中的内容
    print(target['translateResult'][0][0]['tgt'])

    time.sleep(3) #延迟时间提交 使得更像是人类访问
"""
修改heads模拟正常的浏览器访问有两种方法：
    通过Request的headers参数修改（法一）
    通过Request.add_header()的方法修改（法二）

"""
"""代理
步骤: 1.参数是一个字典{'类型':'代理ip:端口号'}
        proxy_support = urllib.request.ProxyHandler({})
      2.定制、创建一个opener
        opener = urllib.request.bulid_opener(proxy_support)  
      3.安装一个opener
        urllib.request.install_openner(opener)    
      4.调用opener
        opener.open(url)
"""