'''
序列常用的BIF
lsit()   把可一个可迭代对象转换为列表
tuple() 把一个可迭代对象转化为元组
len() 返回参数的长度
max() 返回最大的一个参数  使用时必须保证参数的数据类型相同
min() 返回最小的一个参数
sum() 返回序列参数的总和 ，并且还有一个可选参数，结果会在原来数据的基础上加上可选参数
sorted() 排序
reversed() 返回一个倒叙的迭代器
enumerate() 返回一个枚举类型
zip()  合并？？？不好解释 自己看一下结果
'''
a = list()
b = "I Love fishC.com"
b = list(b)
c = (1,1,2,3,5,8,13,21,34)
c = list(c)
print(len(b))
print(max(b))
numbers = [1,18,13,0,-98,54,32,48]
print(min(numbers))
tuple1 = (3.1,2.5,7.5,6.6)
print(sum(tuple1))
print(sorted(tuple1))
print(reversed(numbers))
print(list(reversed(numbers)))
print(enumerate(numbers))
print(list(enumerate(numbers)))
x1 = [1,2,3,4,5,6,7,8]
x2 = [4,5,6,7,8]
print(list(zip(x1,x2)))
