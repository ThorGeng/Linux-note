"""用Python设计第一个游戏哦"""

temp = input("不妨猜一下我现在在想哪个数字？")
guess = int(temp)

if guess == 8:
    print("你是为我心里的蛔虫吗？")
    print("猜中也没有奖！")
else:
    print("猜错了，我心想的是8")

print("游戏结束，不玩了！")
