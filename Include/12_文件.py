'''open函数
第一个参数：文件名
第二个参数：打开的方式
    r:  以只读方式打开文件（默认）
    w:  以写入的方式打开文件，会覆盖已存在的文件如果文件已经存在，使用此模式打开将引发异常
    a:  以写入模式打开，如果文件存在，则在末尾追加写入
    b:  以二进制模式打开文件
    t:  以文本模式打开（默认）
    +:  可读写模式（可添加到其他模式中使用）
    u:  通用换行符支持

    f.close()	关闭文件
    f.read([size=-1])	从文件读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回
    f.readline([size=-1])	从文件中读取并返回一行（包括行结束符），如果有size有定义则返回size个字符
    f.write(str)	将字符串str写入文件
    f.writelines(seq)	向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
    f.seek(offset, from)	在文件中移动文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
    f.tell()	返回当前在文件中的位置
    f.truncate([size=file.tell()])	截取文件到size个字节，默认是截取到文件指针当前位置
'''
f = open(r"D:\python\Python学习\venv\Include\12_txt1.txt")  #open函数返回一个文件对象
print(f)
# print(f.read(),end="\n--------------文件结束--------------") #默认会读取到文件的末尾
# print(f.read()) #因为指针已经读取到文件的末尾了 再读就读不出东西了
print(f.read(3))
print(f.tell()) #返回当前为文件的指针 以字节方式

print(f.seek(20,0))
print(f.tell())
print(f.readline())

'''也可以把文件对象直接转化为列表'''
fileList = list(f)
print(fileList)
f.seek(0,0)

'''用for迭代文件'''
for each_line in f:
    print(each_line)

'''写入模式'''
f = open(r"D:\python\Python学习\venv\Include\12_txt2.txt","w")  #以写入的方式访问一个文件，没有的话会新建一个
f.write("我在通过小甲鱼的视频学Python")    #这个函数会返回写入的字符数
f.close()   #写入的文件一定要记得关闭
