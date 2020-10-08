'''set集合  当{}内的数据没有体现出映射关系，那么这个数据的类型就是集合'''
set1 = {1,2,3,4,5}
print(type(set1))
set2 = {1,2,3,4,4,4,4,5,5,6,8,8,8,6,6,6,6,6,7,7,7,7,7,8,8,8,}
print(set2) #集合中的元素是唯一的  会剔除重复的元素

"可以利用集合的特性剔除列表中重复的元素 缺点是得到的列表是无序的 跟原先不一样"
list1 = [1,1,2,3,4,8,5,5,6,7,8,8,9,6]
list1 = list(set(list1))
print(list1)

'''可以利用成员关系操作符判断一个元素是否在集合中'''
print(8 in set2)
print(80 in set2)

'''利用for循环读取集合中的元素'''
for item in set1:
    print(item,end=" ")
print()

'''add() 和 remove()'''
set2.add(90)
set2.remove(6)
print(set2)

'''定义一个不可变的集合'''
set3 = frozenset([1,2,3,4,5,7,8,9,10])
#set3.add(6) #因为set3是不可变集合 所以这里会报错 AttributeError: 'frozenset' object has no attribute 'add'
print(set3)