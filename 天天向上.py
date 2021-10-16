#使用者：姜海波
#创建时间：2021 / 8 / 6
#14: 40
'''dayup=1.0
dayfactor=0.01
for i in range(365):
    if i % 7 in [0,6]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("工作日的力量：{:.2f}".format(dayup))

weekstr='星期一星期二星期三星期四星期五星期六星期日'
weeKID=eval(input('请输入星期数字1-7:'))
pos=(weeKID-1)*3
print(weekstr[pos:pos+3])'''

'''import random
str1='asoifihoi'
print(str.strip('i'))#从str中去掉在其左右侧chars中列出的字符
stra=r'aso\a'
c=random.randint(1,2)#引入模块，生成随机整数，从int a到int b，两边都包括了
print(c)
j=465
b=str(j)
print(b)
print(dir(list))'''

#汉诺塔
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将n-1个盘子从x移动到y
        print(x,'-->',z)#将最后一个盘子移动到z上去
        hanoi(n-1,y,x,z)#将y上的盘子都移动到z上去

hanoi(5,'x','y','z')