#使用者：姜海波
#创建时间：2021 / 9 / 19
#17: 24
'''from random import random
from time import perf_counter
darts=1000*1000
hits=0.0
start=perf_counter()
for i in range(1,darts):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/darts)
print('圆周率值是：{}'.format(pi))
print("运行时间是：{:.5f}".format(perf_counter()-start))'''


import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):#把布尔值赋给draw，从而决定了是否画下
    drawGap()
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0, 2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):#日期相关的函数
    turtle.pencolor("red")
    for i in date:
        if i =='-':
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i=='=':
            turtle.write("月",font=("Arial",18,"normal"))
        elif i == '+':
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
