'''算数运算符'''
print(-3**2) # **幂运算符  比左边的优先级要低  比右边的优先级要高  所以前两个得到的结果不一样 侯敏两个表达式结果一样
print((-3)**2)
print(3**-2)
print(3**(-2))
'''逻辑运算符'''
print( True and False)
print( True or False)
print(not True or True)
print(not (True or True))
#特别的Python支持 3<5<9 等价于 3<5 and 5<9
a = 3
b = 5
c = 9
print(a < b < c)
print(a < b and b < c)
print(a > b < c)
print(a > b and  b < c)
'''类型判断函数'''
a = 4;
print(type(a))
print(isinstance(a,int))
'''三元操作符'''
a = 3
b = 4
small = a if a < b else b
print("small = " + str(small))
'''断言'''
assert a < b #如果为真程序继续执行 不为真程序抛出运行时异常