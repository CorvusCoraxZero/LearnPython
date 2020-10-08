import sys

'''设置递归的深度（需要导入sys包）'''
sys.setrecursionlimit(10000)

'''求阶乘'''
def loopFactorial(n): #循环版本
    sum = 1
    for x in range(1,n+1):
        sum *= x
    return sum

def recursion1Factorial(n): #递归版本
    if n != 1:
        return n*recursion1Factorial(n-1)
    else:
        return 1

print(loopFactorial(10))
print(recursion1Factorial(10))

'''斐波那契数列'''
def loopFab(num):
    pro1 = 1
    pro2 = 1
    now = 0
    if 0 < num < 2:
        return 1
    for x in range(num-2):
        now = pro1 + pro2
        pro1 = pro2
        pro2 = now
    return now

def recursion1Fab(num):
    if num == 1 or num == 2:
        return 1
    else:
        return recursion1Fab(num-2) + recursion1Fab(num-1)

print("fab=",loopFab(10))
print("fab=",recursion1Fab(10))

'''汉诺塔'''
def hanoTower(num):
    foot = 0
    def hano(n,local,aim,temp):
        nonlocal foot
        foot += 1
        if n == 1:
            print(n, "从",local,"移动到了", aim)
        else:
            hano(n - 1,local,temp,aim)
            print(n, "从", local, "移动到了", aim)
            hano(n - 1, temp, aim, local)

    hano(num, "X", "Z", "Y")
    print("总计：",foot,"步")

hanoTower(64)
