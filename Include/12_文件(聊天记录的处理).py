def save_file(talker1,talker2,count):
    file_name_talker1 = r'D:\python\Python学习\venv\Include\12_文件(聊天记录的处理)\12_文件(聊天记录的处理)talker1-' + str(count) + '.txt'
    file_name_talker2 = r'D:\python\Python学习\venv\Include\12_文件(聊天记录的处理)\12_文件(聊天记录的处理)talker2-' + str(count) + '.txt'

    talker1_file = open(file_name_talker1, 'w')
    talker2_file = open(file_name_talker2, 'w')

    talker1_file.writelines(talker1)  # 写入数据 关闭文件
    talker2_file.writelines(talker2)
    talker1_file.close()
    talker2_file.close()

    talker1 = []  # 清空列表
    talker2 = []

f = open(r"D:\python\Python学习\venv\Include\12_文件(聊天记录的处理)\12_文件(聊天记录的处理)record.txt")

talker1 = []
talker2 = []
count = 1

for each_line in f:
    if each_line[:6] != '＝＝＝＝＝＝' :   #如果该行不是分割行 当读到文件结尾的时候 readLine会返回一个空的字符串
        # 进行分割
        (role,line_spoken) = each_line.split(":",1) #以冒号做分隔符 最多分割1次
        if role == "小甲鱼":
            talker1.append(line_spoken)
        if role == "小客服":
            talker2.append(line_spoken)
    else:
        # 进行保存操作
        save_file(talker1,talker2,count)
        count += 1
save_file(talker1,talker2,count)

f.close()   #关闭文件