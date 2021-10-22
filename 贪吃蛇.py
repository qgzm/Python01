# 使用者：姜海波
# 创建时间：2021/10/21  23:33
#定义一个类
class Point:
    row=0
    col=0
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def copy(self):
        return Point(row=self.row,col=self.col)

'''
left=c*width    top=r*height
'''
#初始化框架
import pygame
import  random
#初始化
pygame.init()
W=800       #设置窗口大小
H=600

Row=60       #行
Col=80      #列
size=(W,H)
window=pygame.display.set_mode(size)   #设置大小用到的     显示相关的用dispaly
pygame.display.set_caption('贪吃蛇')        #设置标题

head=Point(row=int(Row/2),col=int(Col/2))
snakes=[Point(row=head.row,col=head.col+1),Point(row=head.row,col=head.col+2),Point(row=head.row,col=head.col+3)]

def gen_food():
    while True:
        is_coll=False
        pos=Point(row=random.randint(0,Row-1),col=random.randint(0,Col-1))
        if head.row==pos.row and head.col==pos.col:
            is_coll=True
        for snake in snakes:
            if snake.col==pos.col and snake.row==pos.row:
                is_coll=True
                break
        if not is_coll:
            break
    return pos
bg_color=(255,255,255)
#定义坐标
head_color=(0,128,128)
food=gen_food()
food_color=(255,0,0)
snake_color=(200,200,200)
direct='left'       #定义方向,默认是向左


def rect(point,color):
    cell_height=H/Row
    cell_width=W/Col
    left=point.col*cell_width
    top=point.row*cell_height
    pygame.draw.rect(window,color,(left,top,cell_width,cell_height))
    pass
#游戏循环
quit=True
clock=pygame.time.Clock()   #游戏时间控制
while quit:
    #handking events
    for event in pygame.event.get():    #获取事件队列
        #print(event)将会打印各种事件,包括鼠标移动,点击等等
        if event.type==pygame.QUIT:
            quit=False
        elif event.type==pygame.KEYDOWN:        #键盘按下
         #   print(event)
            if event.key==119 or event.key==1073741906:
                if direct=='left' or direct=='right':
                    direct='up'
            elif event.key == 115 or event.key == 1073741905:
                if direct == 'left' or direct == 'right':
                    direct = 'down'
            elif event.key == 97 or event.key == 1073741904:
                if direct == 'up' or direct == 'down':
                    direct = 'left'
            elif event.key == 100 or event.key == 1073741903:
                if direct == 'up' or direct == 'down':
                    direct = 'right'
    eat=(head.row==food.row and head.col==food.col)

    if eat:
        food = Point(row=random.randint(0, Row - 1), col=random.randint(0, Col - 1))
    #处理身子
    #1.把原来的头,插入到snakes的头上
    snakes.insert(0,head.copy())
    if not eat:
        snakes.pop()
    #移动
    if direct=='left':
        head.col-=1
    elif direct=='right':
        head.col+=1
    elif direct == 'up':
        head.row-= 1
    elif direct == 'down':
        head.row += 1

    #检测是否撞墙或者撞住自己
    dead=False
    #撞墙
    if head.col<0 or head.row<0 or head.col>=Col or head.row>=Row:
        dead=True
    for snake in snakes:
        if head.col==snake.col and head.row==snake.row:
            dead=True
            break
    if dead:
        print('游戏结束')
        quit=False
    #render渲染---画出来
    pygame.draw.rect(window,bg_color,(0,0,W,H))         #绘画方块,在窗口里,颜色用rgb
    #绘制蛇头
    for snake in snakes:
        rect(snake,snake_color)
    rect(head,head_color)
    rect(food,food_color)

    pygame.display.flip()   #让出控制权,交还系统
    #set frequency
    clock.tick(30)  #the refresh rate is equivalent to being set to sixty--->sleep(1000/60)


