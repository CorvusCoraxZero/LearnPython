"""迭代器"""
"""
迭代器有两个BIF对应两个魔法方法
  iter()  __iter__() 返回一个迭代器对象
  next()  __next()__ 设定迭代的规则
"""
string = "我要学Python"
it = iter(string) #返回string的迭代器
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #迭代器结束了继续next的话会报StopIteration异常

for ch in string:
    print(ch,end="")

it = iter(string)
while True: #猜测for语句工作原理
    try:
        each = next(it)
    except StopIteration:
        break
    print(each,end="")

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fibs = Fibs()
for each in fibs:
    if each > 50:
        break
    print(each, end=" ")