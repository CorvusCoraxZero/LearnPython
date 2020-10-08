"""模块是更高级的封装
容器 是对 数据的封装
函数 是对 语句的封装
类   是对 方法和属性的封装
模块 就是 程序！
"""

"""导入模块"""
# #方法1
# import modulesPractice
#
# print("32摄氏度,等于华氏度：",modulesPractice.ctof(32))
# print("99摄氏度,等于摄氏度：",modulesPractice.ftoc(99))

# #方法2 强烈不建议
# from modulesPractice import *
#
# print("32摄氏度,等于华氏度：",ctof(32))
# print("99摄氏度,等于摄氏度：",ftoc(99))

#方法3 强烈建议
import modulesPractice as p

print("32摄氏度,等于华氏度：",p.ctof(32))
print("99摄氏度,等于摄氏度：",p.ftoc(99))


"""
if __name__ == '__main__':
    如果该模块作为主程序调用 则__name__变量会返回 '__main__'
    如果作为模块调用会返回 '模块的名字'
    可以以此来判断该模块是作为主程序被调用，还是作为模块被导入
    常用于模块的测试方法前 防止在主程序中跑出模块中的测试方法 例：modulesPractice.py
"""

"""搜索路径 推荐放在site-packages"""
import sys
print(sys.path)
#sys.path.append(r"D:\python\abc") #可以通过这样的方式增加搜索路径

"""
包：
    1.创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字
    2.在文件夹汇总创建一个__init__.py的模块文件，内容可以为空
    3.将相关的模块放入文件夹中
    
    导入时 import 包名.类名 即可   
"""
