brand = ["李宁","耐克","阿迪达斯","鱼C工作室"]
slogan = ["一切皆有可能","JUST DO IT","Impossible is noting","让编程改变世界"]
print("鱼C工作室的口号是：",slogan[brand.index('鱼C工作室')])

"字典 注意：字典不是序列类型，它是映射类型"
dict1 = {"李宁":"一切皆有可能","耐克":"JUST DO IT","阿迪达斯":"Impossible is noting","鱼C工作室":"让编程改变世界"}
print("鱼C工作室的口号是：",dict1["鱼C工作室"])

"创建一个字典"
dict2 = {}
dict3 = dict(((0,"zero"),(1,"one"),(2,"two"),(3,"three"))) #之所以括号里再套个括号是因为dict()只有一个参数
dict4 = dict(花花="flawer",钢笔="pencil",尺子="ruler")
print(dict4)
dict4["钢笔"] = "pen"             #有存在的键会改变值
dict4["橡皮擦"] = "eraser"         #没有存在的键会创建一个项
print(dict4)

'''字典的内置方法

'''
dict5 = {}
print(dict5.fromkeys((1,2,3))) #常见并返回新的字典 有两个参数 一个是字典的键 另一个是字典的值（这个值是可选的，不提供的话默认就是none）
print(dict5.fromkeys((1,2,3),("one","two","three"))) #第二个参数只能提供一个  所有的键对应的都是这个值
dict5 = dict5.fromkeys(range(32),"赞")
for eachKey in dict5.keys():        #访问字典中所有的键
    print(eachKey,end=" ")
print()
for eachValue in dict5.values():    #访问字典中所有的值
    print(eachValue,end=" ")
print()
for eachItem in dict5.items():       #访问字典中所有的项
    print(eachItem,end=" ")
print()

'get方法'
# print(dict5[50])      #访问字典中不存在的项  用该方法会报错
print(dict5.get(50))    #用get方法就不会 会返回一个none

'当不确定字典中是否有该键时  可以使用成员关系操作符来判断'
print(30 in dict5)
print(50 in dict5)

'copy（）方法 copy方法是浅拷贝'
dict6 = dict5.copy()

'''pop 和 popitem'''
dict6.pop(2)  #弹出键对应的值 并从字典中清除该项
dict6.popitem()     #popitem的弹出是随机的

'''setdefault 会返回对应键的值 如果没有会自动添加 这个值可以手动设置'''
print(dict6.setdefault(2,"fafa"))
print(dict6.setdefault(2))

'''update 用一个字典的映射关系，更新另一个字典'''
dict5.update(dict6)  #这里使用dict6的映射关系 更新dict5
print(dict5)

'清空字典建议使用clear()方法'
dict5.clear()
print(dict5)




