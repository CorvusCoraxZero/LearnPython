"""定制容器"""
"""定义一个不可变的列表，要求可以记录列表中的元素被访问的次数 """
class CountList:
    def __init__(self, *args):
        self.value = [x for x in args ]
        self.count = {}.fromkeys((self.value),0)

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        temp = self.value[key]
        print(self.count)
        self.count[temp] += 1
        return temp

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)

print(c1[1] + c2[1])
print(c1.count)