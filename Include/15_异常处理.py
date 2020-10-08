import os

try:
    # int('abc')
    #
    # sum = 1 + '1'

    f = open("我为什么是一个文件")
    print(f.read())
    f.close()
except OSError as reason:
    print("文件出错啦o(╥﹏╥)o ")
    print("错误的原因是" + str(reason))
except TypeError as reason:
    print("错误的原因是" + str(reason))

try:
    num = 1/0
except:         #这样子写回捕获所有的异常 （不推荐）
    print("出错啦！！！")


try:
    sum = 1 + '1'

    f = open("我为什么是一个文件")
    print(f.read())
    f.close()
except (OSError,TypeError) as reason:   #这样子可以对多个异常同时捕获处理
    print("错误的原因是" + str(reason))

try:
    f = open("我为什么是一个文件","w")
    num = 1/0
    f.read()
except (ZeroDivisionError,OSError) as reason:
    print("错误的原因是" + str(reason))
finally:
    print("你错或不错我都会执行！")
    f.close()
    os.remove("我为什么是一个文件")

"raise语句可以手动抛出一个异常"
try:
    raise RuntimeError("这是我手动抛出的异常")
except RuntimeError as reason:
    print("出现异常啦")
    print(reason)

"""read一个可能不存在的文件写法 嵌套try 或者 使用 with语句（推荐）"""
try:
    f = open("这是一个不存在的文件","r")
    try:
        for line in f:
            print(line)
    finally:
        f.close()
except OSError:
    print("读取文件发生错误")
"""
异常种类：
AssertionError	断言语句（assert）失败
AttributeError	尝试访问未知的对象属性
EOFError	用户输入文件末尾标志EOF（Ctrl+d）
FloatingPointError	浮点计算错误
GeneratorExit	generator.close()方法被调用的时候
ImportError	导入模块失败的时候
IndexError	索引超出序列的范围
KeyError	字典中查找一个不存在的关键字
KeyboardInterrupt	用户输入中断键（Ctrl+c）
MemoryError	内存溢出（可通过删除对象释放内存）
NameError	尝试访问一个不存在的变量
NotImplementedError	尚未实现的方法
OSError	操作系统产生的异常（例如打开一个不存在的文件）
OverflowError	数值运算超出最大限制
ReferenceError	弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
RuntimeError	一般的运行时错误
StopIteration	迭代器没有更多的值
SyntaxError	Python的语法错误
IndentationError	缩进错误
TabError	Tab和空格混合使用
SystemError	Python编译器系统错误
SystemExit	Python编译器进程被关闭
TypeError	不同类型间的无效操作
UnboundLocalError	访问一个未初始化的本地变量（NameError的子类）
UnicodeError	Unicode相关的错误（ValueError的子类）
UnicodeEncodeError	Unicode编码时的错误（UnicodeError的子类）
UnicodeDecodeError	Unicode解码时的错误（UnicodeError的子类）
UnicodeTranslateError	Unicode转换时的错误（UnicodeError的子类）
ValueError	传入无效的参数
ZeroDivisionError	除数为零"""