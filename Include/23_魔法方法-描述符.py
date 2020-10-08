"""描述符就是就某种特殊类型的的类的实例指派给另一个类的属性"""
class MyDescriptor:
    def __get__(self,instance,owner):
        print("getting.....",self,instance,owner)
    def __set__(self,instance,value):
        print("setting.....",self,instance,value)
    def __delete__(self, instance):
        print("deleting....",self,instance)

class Test:
    x = MyDescriptor() #此时就称MyDescriptor是x的描述符

test = Test()
test.x
test.x = "X-man"
del test.x

"""propertiy其实就是一个描述符类"""
class MyProperty:
    def __init__(self,fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self,instance,owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance,value)

    def __delete__(self,instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self,value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX,setX,delX)

c = C()
c.x = "x-man"
print(c.x)
del c.x
# print(c.x) #成功删除：AttributeError: 'C' object has no attribute '_x'

"""应用"""
class Calsius:
    def __init__(self,value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Calsius() #摄氏度描述类
    fah = Fahrenheit()

temp = Temperature()
temp.cel = 30
print(temp.fah)
temp.fah = 100
print(temp.cel)