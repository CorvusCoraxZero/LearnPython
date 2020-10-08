''''创建列表'''
member = ["小甲鱼","小布丁","黑夜","迷途","怡静"]
print(member)
number = [1,2,3,4,5,6]
print(number)
mix = [1,"huahua",3.14,["大笨蛋","臭宝宝","小傻逼"]] #列表中可以添加不同类型的元素，甚至是另一个列表
print(mix)
#创建一个空列表
blank = []
print(type(blank))

'''向列表添加元素'''
member.append("The_zero")
print(member)
print(" 长度是"+str(len(member)))
member.extend(["花花","小小仓鼠"]) #extend把一个列表中的元素加入另一个列表里
print(member)
member.insert(1,"小怪兽") #insert将一个元素放进指定的位置
print(member)

'''获取列表元素'''
print(member[1])
temp = member[0] #交换位置
member[0] = member[1]
member[1] = temp
print(member[0])

'''从列表删除元素'''
member.remove("怡静")#通过元素删除，不需要知道位置
del member[7]
print(member)
print(member.pop())
print(member)

'''列表分片'''
print(member[1:3]) #得到1-2的元素 3不包含进来
print(member[:3]) #得到0-2的元素
print(member[3:]) #得到3-结尾的元素
print(member[:]) #得到列表的拷贝

'''比较操作符'''
list1 = [1234]
list2 = [5675]
print(list1 > list2)
list1 = [123,456]    #只要有一个赢了后面的都不需要比较，跟字符串类似
list2 = [456,123]
print(list1 > list2)
list3 = [123,456]
print((list1 < list2) and (list1 == list3) )

'''运算操作符'''
list4 = list1 + list2
x = list4[:]

'''重复操作符'''
print(x)
print(x * 3)
list4 *= 3
print(list4)

'''成员关系操作符'''
print(123 in list1)
print(123 not in member)
list5 = [123,["fafa","benben"],456]
print("fafa" in list5) #看能不能判断列表中的列表的元素  答案是False
print("fafa" in list5[1])


print(list4.count(123))  #count()查看元素出现次数
print(list4.index(123))  #index()查看元素出现的位置
print(list4.index(123),3,8)  #查看123出现的位置，从3开始数，到8结束
print(member)
print(member.reverse())  #将列表元素翻转
list6 = [7,4,2,8,4,9,7,8,2,3]
print(list6.sort())  #列表元素排序
print(list6.sort(reverse=True))