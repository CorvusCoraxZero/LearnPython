import urllib.request
import os
import base64
import time

def url_open(url):  # 返回未解码的网页的html
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23  # 这是查找当前页码的方法 以后会用正则表达式来简化
    b = html.find(']',a)

    return int(html[a:b])

def find_imgs(url):  # 返回找到所有的图片的地址
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('<img src=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)  # 设定只找jpg格式的， 怕找的太远找到下一个紧迫感图片上去，加了个范围255
        if b != -1:  # 找到了
            img_addrs.append(html[a + 10:b + 4])
        else:
            b = a + 9

        a = html.find('<img src=',b)

    # print(img_addrs)
    return img_addrs

def save_imgs(img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]  # 按 / 分割 取最后一个 即是文件的名字
        with open(filename,'wb') as f:
            # img = url_open(each)
            response = urllib.request.urlopen('https:' + each)
            img = response.read()
            f.write(img)

def decodeb64(string):
    string = base64.b64decode(string).decode("utf-8")
    return string


def encodeb64(string):
    bytes_string = string.encode()
    string = base64.b64encode(bytes_string)  # 被编码的参数必须是二进制数据
    return string.decode('utf-8')


def download_mm(floder='妹子图', pages=1):  # pages表示往下爬取的页数
    try:
        os.mkdir(floder)
    except FileExistsError:
        pass

    os.chdir(floder)

    url = "http://jandan.net/ooxx/"
    page_num = get_page(url)
    for i in range(pages):
        page_num -= i
        # 网址url的格式是http://jandan.net/ooxx/+日期(如：20201009）+ -页数
        page_url = url + encodeb64(time.strftime('%Y%m%d') + '-' + str(page_num))
        # print(page_url)
        img_addrs = find_imgs(page_url)  # 保存的是图片的url
        save_imgs(img_addrs)


if __name__ == '__main__':
    download_mm()

