import keyword
print(keyword.kwlist)
a,b,c=1,2,3
print(a,b,c)
a,b,c=c,a,b
print(a,b,c)
s=0
a=0
while a<=4:
    s+=a
    a+=1
print('和为',s)
for x in range(3):
    s=input("请输入密码")
    if s=='123':
        print('密码正确')#TODO('wej')
        break
    else:
        print("密码不正确")
a=0
while a<3:
    '''条件执行体'''
    w=input('请输入密码:')
    if w=="123":
        print('密码正确')
        break
    else:
        print('密码不正确')
        a+=1