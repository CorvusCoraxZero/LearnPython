"""定制一个定时器的类"""
import time as t

class MyTimer():
    def __init__(self):
        self.unit = ['年','月','日','时','分','秒']
        self.prompt = "未开始计时"
        self.lasted = []
        self.start = 0
        self.stop = 0

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return __str__(self)

    def __add__(self,other):
        promt = "两者相加，总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            #进位 月按30天算
            #这里应该有进位 但是没有实现该功能
            if result[index]:
                promt += (str(result[index]) + self.unit[index])
        return promt

    #开始计时
    def startCount(self):
        self.start = t.localtime()
        self.prompt = "提示:请先调用 stopCount() 停止计时"
        print("开始计时")

    #停止计时
    def stopCount(self):
        if not self.start:
            self.prompt = "提示:请先调用stratCount开始计时"
        else:
            self.stop = t.localtime()
            print("停止计时")
            self._calc()

    #内部方法计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            if self.lasted[index] != 0:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        #为下一轮计算初始化
        self.start = 0
        self.stop = 0

a = MyTimer()
a.startCount()
while(1):
    if int(input("输入0停止a计时")) == 0 :
        break
a.stopCount()
print(a)
b = MyTimer()
b.startCount()
while(1):
    if int(input("输入0停止b计时")) == 0 :
        break
b.stopCount()
print(b)
print(a + b)
