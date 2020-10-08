"""属性访问"""
class C:
    def __init__(self):
        self.x = "X-man"

c = C()
getattr(c,'x',"没有这个属性")
getattr(c,'p','没有这个属性')

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

c = C()
print(c.x)
c.x = 20
print(c.x)
print(c.x)
del c.x
# print(c1.getSize()) #AttributeError: 'C' object has no attribute 'size'
"""魔法方法"""
class C:
    def __getattribute__(self, item):
        print("getattribute")   #定义该类的属性被访问时的行为  当没有找到时 会执行__getattr__
        return super().__getattribute__(item)
    def __getattr__(self, item):  #当用户试图获取一个不存在的属性时调用的方法
        print("getattr 当访问的属性和不存在时我就会执行")
    def __setattr__(self, key, value):
        print("setattt")
        return super().__setattr__(item,value)
    def __delattr__(self, item):
        print("delattr")
        return super().__delattr__(item)
c = C()
c.x

"""实例"""
class Retangle:
    def __init__(self,length = 0,width = 0):
        self.length = length
        self.width = width
    def __setattr__(self, key, value):
        if key == "square":
            self.width = value
            self.length = value
        else:
            # super().__setattr__(key,value) #调用基类的赋值方法（推荐）
            self.__dict__[key] = value #对数据的字典进行赋值
    def getArea(self):
        return self.width * self.length

r1 = Retangle(4,5)
print(r1.getArea())
r1.square = 10
print(r1.getArea())
print(r1.__dict__)