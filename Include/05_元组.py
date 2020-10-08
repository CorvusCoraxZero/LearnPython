'''创建元组'''
tuple1 = (1,2,3,4,5,6,7,8)
print(tuple1)

'''元组分片'''
print(tuple1[1:4])
print(tuple1[5:])
print(tuple1[:5])
tuple2 = tuple1[:3]

'''元组的值不可以被改变'''
#tuple1[2] = 8 #会报错  TypeError: 'tuple' object does not support item assignment

'''元组的标志符号是--》 ，逗号  '''
tuple3 = (1)
print(type(tuple3)) #<class 'int'>
tuple3 = (1,)
print(type(tuple3)) #<class 'tuple'>
tuple4 = 1,
print(type(tuple4)) #<class 'tuple'>
#创建一个空元祖
tuple5 = ()
print(type(tuple5)) #<class 'tuple'>
#用重复操作符来证明逗号的决定性作用
print(8*(7,))

'''元组的更新'''
tuple6 = ("我","觉","得","，","我","你")
tuple6 = tuple6[:5]+("喜欢",)+tuple6[5:]
print(tuple6)

'''元组的删除，方法同元组的更新，删除整个元组可以使用del语句'''
del tuple6
#print(tuple6)

'''其他列表能用的操作符 元组也可以用'''