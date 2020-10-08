"""生成器 生成器是一种特殊的迭代器 生成器的出现使得协同程序的概念得以实现"""
"""协同程序就是可以运行的独立函数调用，函数可以展厅或者挂起，并在需要的时候从函数离开的地方继续或者重新开始"""
def myGen():
    print("生成器被执行！")
    yield 1
    yield 2

myG = myGen()
print(next(myG))
next(myG)

myG = myGen()
for i in myG:
    print(i)

"""用生成器写一个feb数列"""
def feb():
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        yield a

for i in feb():
    if(i < 100):
        print(i ,end=" ")
    else:
        break
print("")

"""列表推导式"""
a = [i for i in range(100) if not(i % 2) and i % 3] #100以内可以被2整除但是不能被3整除的数
print(a)
"""字典推导式"""
b = {i:i % 2 == 0 for i in range(10)} #10因为可以被2整除的数 可以为True 不可以为False
print(b)
"""集合推导式"""
c = {i for i in [1,1,2,3,4,4,5,5,6,6,7,7,7,7,8,9,9,10,10]}
print(c)
"""元组推导式？ 不！ 这是生成器推导式"""
e = (i for i in range(10))
print(e)
for each in e:
    print(each, end=" ")
print("")

"""生成器推导式可以直接写在函数的参数上"""
print(sum(i for i in range(100) if i % 2 ))