""" if-else要么这样，要么不怎样"""
if(1 < 0):
    print("这是不可能滴")
else:
    print("1怎么可能小于0呢？？？")

"""while-else 干完了能怎样，干不完就别想怎样"""
import math
def showMaxFactor(num):
    count = math.sqrt(num)
    while count > 1:
        if num % count == 0:
            print("%d最大的数是%d" % (num,count))
            break
        count -= 1
    else:
        print("%d是素数" % num)

num = input("请输入一个整数")
showMaxFactor(int(num))

"""try-exception-else 没有问题，那就干吧"""
try:
    int("123")
except ValueError as reason:
    print("出错啦"+str(reason))
else:
    print("没有任何异常！")

"""with语句"""
try:
    with open("data.txt","w") as f: #with语句会自动关闭文件 这样就不用写 finally来关闭文件
        for each_line in f:
            print(each_line)
except OSError as reason:
    print("出错啦" + str(reason))
# finally:
#     f.close()

try:
    with open("这是一个不存在的文件","r") as f:
        for line in f:
            print(line)
except OSError:
    print("读取文件发生错误")