#使用者：姜海波
#创建时间：2021 / 1 / 16    13: 48
'''要求输出1到50之间5的倍数'''
'''print('使用continue语法')
for i in range(1,51):
    if i%5!=0:
        continue
    print(i)
for x in range(1,5):
    for k in range(1,4):
        print(x,'*',k,end='\t')
    print()

for i in range(1,13):
    for j in range(1,i+1):
        print(i,'*',j,"=",i*j,end='\t')
    print()'''


'''def getNum():
    nums=[]
    iNumStr=input("请输入数字（回车退出）：")
    while iNumStr !=" ":
        nums.append(int(eval(iNumStr)))
        iNumStr=input("请输入数字（回车退出）")
    return nums
def mean(numbers):#平均数
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)

def dev(numbers,mean):#方差
    sdev =0.0
    for num in  numbers:
        sdev=sdev+[(num-mean)**2]
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):#求中位数
    sorted(numbers)
    size =len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[numbers//2]
    return med

n=getNum()
m=mean(n)
print("平均值:{},方差{:.2},中位数:{}".format(m,dev(n,m),median(n)))'''

'''import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
datals=[]
f=open("data.txt")
for line in f:
    line =line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
f.close()
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])'''