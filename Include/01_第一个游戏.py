# temp = input("你猜猜我现在想的数字是什么？？")
# guess = int(temp)
# if guess == 8 :
#     print("你怎么知道我想的就是8！！！")
#     print("wocao!")
# else:
#     print("哦吼~  猜错了哟~")
# print("结束啦~~")
"""
BIF = Built-in functions 内置函数
例如 input int print
在IDLE输入dir(__builtins__)可以知道所有的BIF
"""
print("C:\now")
print(r"C:\now") #在字符串前加上r表示该字符串是原始字符串 没有转义符
str = r"C:\now"  #在内存里 str = C:\\now
print(str)
#print(r"C:\now\") 原始字符串结尾不能加\不然会发生语法错误
print(r"C:\now"+"\\")# 非要加\的解决办法#print(r"C:\now\")

print("我爱我的臭宝宝"
      "翁子婷"
      "虽然她很臭臭"
      "但我还是喜欢他")#跨行的文本可以用三个引号括起来 输出就会分行 内存中的形式是\n
print("""我爱我的臭宝宝
翁子婷
虽然她很臭臭
但我还是喜欢她""")

