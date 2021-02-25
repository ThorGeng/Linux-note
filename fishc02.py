"""改进用Python设计第一个游戏
    1.当用户输入错误时，应给出提示
    2.提供多次机会给用户
    3。每次运行程序，答案应该是随机的
"""
import random

counts= 3
ans = 5
while counts > 0:
    temp = input("不妨猜一下我现在在想哪个数字？")
    guess = int(temp)

    if guess == ans:
        print("你是为我心里的蛔虫吗？")
        print("猜中也没有奖！")
        break
    else:
        if guess < ans:
            print("小啦~")
        else:
            print("大啦~")
    counts= counts-1

print("游戏结束，不玩了！")
