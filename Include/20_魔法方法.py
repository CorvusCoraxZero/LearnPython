'''构造和析构'''
'''__new__'''
class CapStr(str):
    def __new__(cls, string): #__new__是对象创建时 第一个被调用的方法 常用于该类继承与一个不可变对象时
        string = string.upper()
        return str.__new__(cls,string)

a = CapStr("I love FishC.com!")
print(a)

'''__del__'''
class C:
    def __init__(self):
        print("我是__init__方法 我被调用了")
    def __del__(self):  #当垃圾回收机制回收该对象时被调用 并不是del X时被调用
        print("我是__del__方法  我被调用了")

c1 = C()
c2 = c1
del c2
del c1

'''对象间的算数运算 add sub mul truediv floordiv mod divmod pow lshift（左移） rshift add xor（异或） or'''
class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)  #给加法定义了一个int减法的算法
    def __sub__(self, other):
        return int.__add__(self,other)  #给减法定义了一个int加法的算法

a = New_int(5)
b = New_int(8)
print(a+b)
print(a- b)

class New_int2(int):    #另一种写法
    def __add__(self,other):
        return int(self) - int(other)  #如果直接return self - other 会进入无限递归
    def __sub__(self, other):
        return int(self) + int(other)

a = New_int(5)
b = New_int(8)
print(a+b)
print(a- b)

'''反运算 当左操作数的运算方法不可用时 就会调用右操作数的反运算方法'''
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self,other) #当反操作调用时 调用减法操作

a = Nint(5)
b = Nint(3)
print(a + b)
print(5 + b)    #这里调用的是__radd__ self是b other是5
"""这里执行反运算方法的原因是：
    如果右操作数的类型是左操作数类型的子类，   
    并且该子类提供了操作的反射方法，
    则该方法将在左操作数的左操作数的非反射方法之前被调用"""




"""
__new__(cls[, ...])	
    1. __new__ 是在一个对象实例化的时候所调用的第一个方法
    2. 它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法
    3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 __new__ 没有返回实例对象，则 __init__ 不会被调用
    4. __new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string
__init__(self[, ...])	构造器，当一个实例被创建的时候调用的初始化方法
__del__(self)	析构器，当一个实例被销毁的时候调用的方法
__call__(self[, args...])	允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)
__len__(self)	定义当被 len() 调用时的行为
__repr__(self)	定义当被 repr() 调用时的行为
__str__(self)	定义当被 str() 调用时的行为
__bytes__(self)	定义当被 bytes() 调用时的行为
__hash__(self)	定义当被 hash() 调用时的行为
__bool__(self)	定义当被 bool() 调用时的行为，应该返回 True 或 False
__format__(self, format_spec)	定义当被 format() 调用时的行为

有关属性
__getattr__(self, name)	定义当用户试图获取一个不存在的属性时的行为
__getattribute__(self, name)	定义当该类的属性被访问时的行为
__setattr__(self, name, value)	定义当一个属性被设置时的行为
__delattr__(self, name)	定义当一个属性被删除时的行为
__dir__(self)	定义当 dir() 被调用时的行为
__get__(self, instance, owner)	定义当描述符的值被取得时的行为
__set__(self, instance, value)	定义当描述符的值被改变时的行为
__delete__(self, instance)	定义当描述符的值被删除时的行为

比较操作符
__lt__(self, other)	定义小于号的行为：x < y 调用 x.__lt__(y)
__le__(self, other)	定义小于等于号的行为：x <= y 调用 x.__le__(y)
__eq__(self, other)	定义等于号的行为：x == y 调用 x.__eq__(y)
__ne__(self, other)	定义不等号的行为：x != y 调用 x.__ne__(y)
__gt__(self, other)	定义大于号的行为：x > y 调用 x.__gt__(y)
__ge__(self, other)	定义大于等于号的行为：x >= y 调用 x.__ge__(y)

算数运算符
__add__(self, other)	定义加法的行为：+
__sub__(self, other)	定义减法的行为：-
__mul__(self, other)	定义乘法的行为：*
__truediv__(self, other)	定义真除法的行为：/
__floordiv__(self, other)	定义整数除法的行为：//
__mod__(self, other)	定义取模算法的行为：%
__divmod__(self, other)	定义当被 divmod() 调用时的行为
__pow__(self, other[, modulo])	定义当被 power() 调用或 ** 运算时的行为
__lshift__(self, other)	定义按位左移位的行为：<<
__rshift__(self, other)	定义按位右移位的行为：>>
__and__(self, other)	定义按位与操作的行为：&
__xor__(self, other)	定义按位异或操作的行为：^
__or__(self, other)	定义按位或操作的行为：|

反运算
__radd__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rsub__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rmul__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rtruediv__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rfloordiv__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rmod__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rdivmod__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rpow__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rlshift__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rrshift__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rand__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__rxor__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）
__ror__(self, other)	（与上方相同，当左操作数不支持相应的操作时被调用）

增量赋值运算
__iadd__(self, other)	定义赋值加法的行为：+=
__isub__(self, other)	定义赋值减法的行为：-=
__imul__(self, other)	定义赋值乘法的行为：*=
__itruediv__(self, other)	定义赋值真除法的行为：/=
__ifloordiv__(self, other)	定义赋值整数除法的行为：//=
__imod__(self, other)	定义赋值取模算法的行为：%=
__ipow__(self, other[, modulo])	定义赋值幂运算的行为：**=
__ilshift__(self, other)	定义赋值按位左移位的行为：<<=
__irshift__(self, other)	定义赋值按位右移位的行为：>>=
__iand__(self, other)	定义赋值按位与操作的行为：&=
__ixor__(self, other)	定义赋值按位异或操作的行为：^=
__ior__(self, other)	定义赋值按位或操作的行为：|=

一元操作符
__pos__(self)	定义正号的行为：+x
__neg__(self)	定义负号的行为：-x
__abs__(self)	定义当被 abs() 调用时的行为
__invert__(self)	定义按位求反的行为：~x

类型转换
__complex__(self)	定义当被 complex() 调用时的行为（需要返回恰当的值）
__int__(self)	定义当被 int() 调用时的行为（需要返回恰当的值）
__float__(self)	定义当被 float() 调用时的行为（需要返回恰当的值）
__round__(self[, n])	定义当被 round() 调用时的行为（需要返回恰当的值）
__index__(self)	
    1. 当对象是被应用在切片表达式中时，实现整形强制转换
    2. 如果你定义了一个可能在切片时用到的定制的数值型,你应该定义 __index__
    3. 如果 __index__ 被定义，则 __int__ 也需要被定义，且返回相同的值

上下文管理（with 语句）
__enter__(self)	
    1. 定义当使用 with 语句时的初始化行为
    2. __enter__ 的返回值被 with 语句的目标或者 as 后的名字绑定
__exit__(self, exc_type, exc_value, traceback)	
    1. 定义当一个代码块被执行或者终止后上下文管理器应该做什么
    2. 一般被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作

容器类型
__len__(self)	定义当被 len() 调用时的行为（返回容器中元素的个数）
__getitem__(self, key)	定义获取容器中指定元素的行为，相当于 self[key]
__setitem__(self, key, value)	定义设置容器中指定元素的行为，相当于 self[key] = value
__delitem__(self, key)	定义删除容器中指定元素的行为，相当于 del self[key]
__iter__(self)	定义当迭代容器中的元素的行为
__reversed__(self)	定义当被 reversed() 调用时的行为
__contains__(self, item)	定义当使用成员测试运算符（in 或 not in）时的行为"""
