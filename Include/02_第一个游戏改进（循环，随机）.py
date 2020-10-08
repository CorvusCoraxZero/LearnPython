import random

# temp = input("你猜猜我现在想的数字是什么？？")
# guess = int(temp)
# num = random.randint(0,11);
# time = 1
# while guess != num  and time <= 3:
#     time+=1
#     if guess > num :
#         print("哦吼~ 大了哟~~")
#     else:
#         print("哦吼~ 小了哟~~")
#     if time <= 3:
#         guess = int(input("猜错了 请重新输入吧"))
# if guess == num  :
#     print("你怎么知道我想的就是" + str(num) +" ！！！")
#     print("wocao!")
# if time > 3:
#     print("啧啧啧  也太没有默契了吧正确答案是"+ str(num) )
# print("结束啦~~")

'''for循环'''
a = [1,2,3,4]
for x in a:
    print(str(x),end='') #end=''设置不换行
print("")
s = "ILOVETHEWORD"
for char in s:
    print(char ,end =' ')
'''for配合range'''
range(5)
print(range(5))
print(list(range(5)))
for i in range(5):
    print(i,end=" ")
print("")
for i in range(0,10):
    print(i,end=" ")
print("")
for i in range(0,10,2):
    print(i,end=" ")
print("")