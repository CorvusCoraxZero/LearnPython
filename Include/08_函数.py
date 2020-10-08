'''创建函数'''
def myFirstFunction():
    print("这是我创建的第一个函数")
    print("啦啦啦啦啦啦")

def mySecoundFunction(name):
    print("我要吃"+name)

def myThirdFunction(name1,name2):
    print("我要吃"+name1+","+name2)

def add(num1,num2):
    '这里写的是函数的文档'
    #我来写点注释
    return num1+num2

def saysome(str1,str2):
    print('str1是：'+ str1)
    print('str2是：' + str2)

def saysome2(str1="我有默认值",str2="不写也可以"):
    print('str1是：'+ str1)
    print('str2是：' + str2)

def test(*params):      #这里参数的类型是收集参数
    print("参数的长度是：",len(params))
    print("第二个参数是：",params[1])

def test2(*params,ex="fafa"):      #如果收集参数后面还有参数，赋值的时候要使用关键字参数赋值（建议收集参数后的参数使用默认值参数）
    print("参数的长度是：",len(params))
    print("ex参数是：",ex)

myFirstFunction()
mySecoundFunction("鸡腿")
myThirdFunction("小鱼干","小虾米")
print(add(8,9))
print(add.__doc__)  #查看函数的文档
help(add)           #用help查看函数的文档

saysome(str2="二号字符串",str1="一号字符串")  #用了关键字参数之后，python就不会按顺序来索引了
saysome2()
saysome2(str2="但是也可以改变")

test(1,2,3,4,5,6,7)
test2(1,2,3,4,5,7,ex="啦啦啦")

'''全局变量 局部变量'''
# def discount(price,rate):
#     final_price = price * rate          #这里的final_price是局部变量
#     #print('这里试图打印全局变量old_price的值',old_price)  #这里会报出异常local variable 'old_price' referenced before assignment
#     old_price = 50       #这里试图修改全局变量old_price，但实际是创建了一个名为old_price的局部变量  这是Python的屏蔽（Shadowing）机制
#     print("1.修改后的old_price的值是",old_price)
#     return final_price
#
# old_price = float(input("请输入商品原价:"))
# rate = float(input("请输入商品折扣:"))
# new_price = discount(old_price,rate)
# print("2.修改后的old_price的值是",old_price)
# print("打折后的价格是:")
#
# def testGlobal():
#     global num      #这样就是声明这是一个全局变量
#     num = num + 1
#     global tt       #在函数中声明一个新的全局变量
#     tt = "在函数中声明的全局变量"
#     print(num)
#
# num = 10
# testGlobal()
# print(num)
# print(tt)

'''内部函数'''
def fun1():
    print("fun1正在被调用")
    def fun2():     #fun2是fun1的内部方法，除了fun1内，其他地方都无法调用
        print("fun2正在被调用")
    fun2()

fun1()

def funX(x):
    def funY(y):
        return x * y  #在一个内部函数里，对外部作用域的变量进行了引用，则说该内部函数是一个闭包
    return funY

#调用闭包
#方法一：
i = funX(10) #这里i的类型是一个函数
print(i(5))
#方法二：
print(funX(10)(5))


def funI(i):
    i = [i]         #这里使用容器的方法 使得在内部方法中可以对外部变量进行更改 这是Python3之前的办法
    def funJ(j):
        # i += j
        # return i  #这里会报错因为i对于funJ来说是一个非全局变量的外部变量 不可以对他进行修改
        i[0] = i[0]+j
        return i[0]
    return funJ

print(funI(10)(5))

def funI(i):
    def funJ(j):
        nonlocal i #Python3新添加的关键字 用法同global 使得闭包可以对外部变量进行修改
        i += j
        return i
    return funJ

print(funI(10)(5))

'''lambda表达式'''
def ds(x):      #普通的函数
    return 2 * x + 1
print(ds(5))
g = lambda x : 2 * x +1 #匿名函数 lambda返回的是一个函数对象
print(g(5))
g = lambda x,y: x + y
print(g(1,4))

'''
lambda应用：
filter() 第一个参数为None的话会筛选出第二个参数中为True的元素 
如果第一个为函数的话会将第二个参数中的元素放入该函数 并返回结果为True的对象'''
print(list(filter(None,[1,0,False,True]))) #fliter()方法返回的是一个迭代器对象
def odd(x):
    return x % 2
print(list(filter(odd,(10,3,5,7,8,6,4))))  #这是一个奇数的过滤器

print(list(filter(lambda x: x % 2,(10,3,5,7,8,6,4))))  #lambda明显简介很多

'''map()会将序列中的元素放入函数中加工返回加工完毕的序列'''
print(list(map(lambda x : x * 2,(1,2,3,4,5))))

