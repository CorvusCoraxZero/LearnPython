import pickle
import os

'''写入'''
my_list  = [123,3.1415926535,"小甲鱼",["another list"]]
# os.mkdir(r".\14_pickle模块练习")
pickle_file = open(r".\14_pickle模块练习\my_list.pkl","wb") #文件的后缀名可以使.pkl 或者 .pickle 注意这里的打开方式一定要是 b 二进制模式
pickle.dump(my_list,pickle_file)    #将数据倒入文件
pickle_file.close()

'''读取'''
pickle_file2 = open(r".\14_pickle模块练习\my_list.pkl","rb")
my_list2 = pickle.load(pickle_file2)
print(my_list2)