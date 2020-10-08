"""继承"""
class Parent:
    def hello(self):
        print("我是Parent的方法.....")

class Child(Parent): #在括号内写上父类的方法名即可继承
    pass

c = Child()
c.hello()

class Child(Parent):
    def hello(self):    #重写父类的方法
        print("我是Child的方法.....")

c = Child()
c.hello()

"""调用父类的构造方法"""
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        self.y -= 1
        print("我的位置是：%3d %3d" % (self.x,self.y))

class GoldFish(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #这是两种调用父类方法的技术  如果不调用父类的构造方法 AttributeError: 'Shark' object has no attribute 'x'
        #Fish.__init__(self)#1.调用未绑定的父类的方法（不推荐）
        super().__init__()      #2.使用super(推荐)

        self.hungry = True

    def eat(self):
        if self.hungry:
            print("我要吃吃吃！！")
            self.hungry = False
        else:
            print("嗝~  好撑吃不下了")

fish1 = Fish()
fish2 = GoldFish()
fish3 = Shark()
fish1.move()
fish2.move()
fish3.move()
fish3.eat()

"""多重继承"""
class Base1:
    def __init__(self):
        self.a = "A"

    def foo1(self):
        print("我是foo1，我为Base1代言")

class Base2:
    def __init__(self):
        self.b = "B"

    def foo2(self):
        print("我是foo2，我为Base2代言")

class C(Base1,Base2):
    def __init__(self):
        super().__init__()

c = C()
c.foo1()
c.foo2()
print(c.a)
# print(c.b)  #AttributeError: 'C' object has no attribute 'b' 说明super().__init__()只调用了第一个父类的构造方法

"""组合"""
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x ,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def printNum(self):
        print("水池中一共有%d只乌龟，和%d只鱼" % (self.turtle.num,self.fish.num))

p = Pool(5, 9)
p.printNum()

"""类，类对象，实例对象"""
class CC:
    count = 0

a = CC()
b = CC()
c = CC()

print("a=%d b=%d c=%d" % (a.count, b.count, c.count))
c.count += 10
print("a=%d b=%d c=%d" % (a.count, b.count, c.count))
CC.count += 100 #这里的a,b虽然是实例对象 但是他们对应的count还是类属性（相当于java的静态属性  ）  修改实例对象的属性时会覆盖 该实例对应的类属性 所以 CC.count+= 100 a,b有变化c没变化
print("a=%d b=%d c=%d" % (a.count, b.count, c.count))


"""如果属性的名字和方法相同"""
class C:
    def x(self):
        print("X-man!")

c = C()
c.x = 1     #如果属性的名字和方法名相同属性名会覆盖方法名
print(c.x)
#c.x()      #因为该方法名被覆盖了  所以发正常引用

"""绑定  Python的方法是强制要求有实例的"""
class CC:
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def printXY(self):
        print(self.x,"  ",self.y)

dd = CC()
print(dd.__dict__)
print(CC.__dict__)
dd.setXY(5,6)
print(dd.__dict__)
del CC          #类中定义的属性和方法都是静态的  就算类对象被删除了 依然存在于内存中 所以可以调用
dd.printXY()

"""一些相关的BIF
issubclass(class,classinfo) 判断class是否是classinfo的子类  
    ps：1.这是非严格的检测，也就是说一个类会被认为是自己的子类
        2.classinfo可以是一个元组
"""
class A:
    pass
class B(A):
    pass
print("issubclass(B,A) ",issubclass(B,A))
print("issubclass(B,B) ",issubclass(B,B))
print("issubclass(B,object) ",issubclass(B,object))

"""
isinstance(object,classinfo) 检查object是否是classinfo的实例
    ps：1.如果第一个参数不是对象会永远返回False
        2.如果第二参数不是类或者类对象的元组，会抛出一个TypeError   
"""
print("isinstance(B,A) ",isinstance(B,A))
b = B()
print("isinstance(b,B) ",isinstance(b,B))
print("isinstance(b,A) ",isinstance(b,A))  #这个类的父类也会返回True
"""
hasattr(object,name)    判断objcet中是否有名为name的属性
getattr(object,name[, default])  获取对象指定的属性值 如果属性值不存在 会返回一个default的值 否则会抛出一个异常
setattr(object,name,value) 为object添加属性值名为name的属性 值为value
delattr(object,name)    删除属性，跟上面的类似
"""
class C:
    def __init__(self,x = 123456):
        self.x = x

c1 = C()
print("hasattr(c1,'x')",hasattr(c1,"x"))
print("getattr(c1,'x') ",getattr(c1,"x"))
print("getattr(c1,'y',[defult]) ",getattr(c1,"y","我是的defult默认值"))

"""property(fget = None, fset = None, fdel = None, doc = None) 通过属性来修改属性"""
class C:
    def __init__(self,size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize,setSize,delSize)

c1 = C()
c1.getSize() #原本的方式
print(c1.x) #获取属性
c1.x = 20   #修改属性
print(c1.x)
del c1.x
# print(c1.getSize()) #AttributeError: 'C' object has no attribute 'size'