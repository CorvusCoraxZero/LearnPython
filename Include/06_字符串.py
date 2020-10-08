#分片
str1 = "I love fishc.com "
print(str1[6:])
#获取单个字符
print(str1[3])
#修改字符串
str1 = str1[:4]+"插入的字符串"+str1[4:]
print(str1)

'''一些常用的方法'''
str2 = "  fafa"
print(str2.capitalize())        #首字母大写
print(str2.center(40))          #填充空格至40长度 并使字符串居中
print(str2.count('a'))          #计算a的次数
print(str2.endswith("fa"))      #检查是否以fa结尾
print(str2.find('fa'))          #查找fa在字符串中的位置  如果没有找到返回-1
print(str2.index('fa'))         #查找fa在字符串中的位置  如果没有找到会弹出一个异常
print(str2.islower())           #判断字符串中是否所有的字符都是小写
print(str2.isspace())           #如果有空格就返回true
print(str2.isnumeric())         #如果字符串只包含数字就返回
print(str2.isupper())           #如果字符串中至少包含一个区分大小写的字符 且这些字符都为大写则返回True
print(str2.join("OOOOOOOOOOO")) #将括号内的字符串用str2隔开
print(str2.lower())             #将str2转化为小写
print(str2.upper())             #将str2转化为大写
print(str2.lstrip())            #去掉字符串开始的空格 rstrip()去掉末尾的空格
print(str2.replace("fa","GG",1))#将str2中的‘fa’替换为GG,执行一次
str3 = "  I Love Weng   "
print(str3.split())             #默认按空格切片
print(str3.split("o"))          #也可以指定按什么切，还有一个参数是最多切多少下
print(str3.strip())             #删除前后的所有空格  也可以给定一个字符串 删除前后出现的这个字符串

'''字符串的格式化'''
print("{0} love {1}.{2}".format("I","fishC","com"))         #位置参数
print("{a} love {b}.{c}".format(a="I",b="fishC",c="com"))   #关键字参数
print("{{0}} love {{1}}.{{2}}".format("I","fishC","com")) #如果过想打印{}需要将他用自己本身括起来
print('{0:.1f}{1}'.format(27.658,"GB"))   #冒号表示格式化符号的开始

print('%c %c %c' % (97,98,99))
print('%s' % "I love Weng")
print('%d + %d = %d' %(4,5,4+5))
print('%X %x' %(10,10))
print('%f'% 3.1415926535)
print('%e'% 3.1415926535)
print('%g'% 3.1415926535)
print('%5.2f'% 3.1415926535)
print('%5.2e'% 3.1415926535)
print('%+8.2f'% 3.1415926535)   #用于在正数前显示正号
print('%-8.2f'% 3.1415926535)   #用于左对齐
print('%#o' % 13)               #井号用于显示进制符号
print('%#x' % 13)               #用于显示进制符号

'''
%c  格式化字符及其 ASCII 码
%s  格式化字符串
%d  格式化整数
%o  格式化无符号八进制数
%x  格式化无符号十六进制数
%X  格式化无符号十六进制数（大写）
%f  格式化浮点数字，可指定小数点后的精度
%e  用科学计数法格式化浮点数
%E  作用同 %e，用科学计数法格式化浮点数
%g  根据值的大小决定使用 %f 或 %e
%G  作用同 %g，根据值的大小决定使用 %f 或者 %E

m.n m 是显示的最小总宽度，n 是小数点后的位数
-   用于左对齐
+   在正数前面显示加号（+）
#   在八进制数前面显示 '0o'，在十六进制数前面显示 '0x' 或 '0X'
0   显示的数字前面填充 '0' 取代空格

\'  单引号
\"  双引号
\a  发出系统响铃声
\b  退格符
\n  换行符
\t  横向制表符（TAB）
\v  纵向制表符
\r  回车符
\f  换页符
\o123  八进制数代表的字符
\x123  十六进制数代表的字符
\0  表示一个空字符
\\  反斜杠
'''