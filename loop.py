import random
import string

for i in range(10):
    print(i)
#range不包括10 0-9

count = 1
randomStr = random.choice(string.ascii_lowercase)
while count<=10:
    content = input("输入:")
    # if content == "a":
    if content == randomStr:
        print("right")
        break
        #exit(0)彻底结束
        # break跳出当前循环
        # continue停止本次循环，直接进入下一次循环
    else:
        print("错误，剩余" + str(10 - count) + "次机会")
        count = count + 1

if count>10:
    print("游戏结束，"+randomStr+"是正确答案。")
else:
    print("成功")

#简单的循环判断，如同学习Java

