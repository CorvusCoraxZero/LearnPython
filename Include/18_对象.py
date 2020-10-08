class Turtle:
    #属性
    color = "green"
    weight = 19
    legs = 4
    shell = True
    mouth = "大嘴"

    #方法
    def climb(self):
        print("我正在很努力的爬")

    def run(self):
        print("溜了 溜了")

    def bite(self):
        print("我生气了 我要咬你")

    def eat(self):
        print("我正在吃东西")

    def sleep(self):
        print("我睡觉啦！")

tt = Turtle()
tt.bite()

class MyList(list): #表示继承list的列表
    pass
my_list = [1,2,6,6,5,1,2,9,7,25]
print(my_list.sort())

class Ball:
    def setName(self,name): #有了set函数 就不用写成员变量了
        self.name = name    #self 就相当于 this
    def kick(self):
        print("我的名字叫%s，该死的，谁踢我" % self.name)

a = Ball()
a.setName("A")
b = Ball()
b.setName("B")
a.kick()
b.kick()

"Python的魔法方法"
" __init__"
class Ball:
    def __init__(self,name = "AA"):#类似于构造函数  可以设置默认参数
        self.name = name
    def kick(self):
        print("我的名字叫%s，该死的，谁踢我" % self.name)

b = Ball("土豆")
b.kick()

"Python实现类成员的私有化"
class Person:
    __name = "小甲鱼"
    def getName(self):  #在类成员前加上下划线就相当于 将该成员设置为私有
        return self.__name

p = Person()
# print(p.__name) #会报错 AttributeError: 'Person' object has no attribute '__name'
print(p.getName())  #需要通过get函数来访问
print(p._Person__name)    #Pyton的私有机制其实是伪私有 通过name mangling机制实现 并没有限制访问 只是改成了_类名__成员名 的形式


class MyClass:
    name = 'FishC'

    def myFun(self):
        print("Hello FishC!")

#MyClass.myFun() #有了self的函数 就需要通过创建对象才能调用  TypeError: myFun() missing 1 required positional argument: 'self'
c = MyClass()
c.myFun()

import random as r

legal_x = [0, 10]
legal_y = [0, 10]


class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
            # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.power:
        print("乌龟体力耗尽，挂掉了！")
        break

    pos = turtle.move()
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            # 鱼儿被吃掉了
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了...")