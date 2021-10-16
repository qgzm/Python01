#使用者：姜海波
#创建时间：2021 / 6 / 27
#20: 34
tempstr=input("请输入温度：")
if tempstr[-1] in ['f','F']:
    c=(eval(tempstr[0:-1])-32)/1.8   #eval 函数 去除参数最外侧引号并执行余下的语句的函数
    print("转换后的温度是{:.2f}c".format(c))
elif tempstr[-1] in ['c','C']:
    f=1.8*eval(tempstr[0:-1])+32
    print('转换后的温度是{:.2f}f'.format(f))
else:
    print('输入错误')