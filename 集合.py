# 使用者：姜海波
# 创建时间：2021/10/21  22:14

#集合没有下标
#append extend insert--->list   有序,允许重复
#add update--->set
list1=[1,3,3,6,34,63,6]     #去掉重复的元素
set2=set(list1)
set1={999}
print('set2:',set2)
set2.add(45)        #添加元素
print("set2添加后:",set2)
set2.update(set1)       #将set1放入set2中
print("将set1加入set2后:",set2)

#产生五组不重复的由字母和数字组成的验证码
#最终打印处来
import random
code_list=set()
s="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
while True:
    code=""
    for i in range(4):
        r=random.choice(s)   #index=random.randint(0,len(s)-1)   code+=s[index]效果一样
        code+=r
    #将code添入set中
    code_list.add(code)
    #判断长度
    if len(code_list)==5:
        break

print(code_list)

#移除元素
set2.remove(3)      #如果元素不存在,会报错
set2.discard(9)         #如果元素不存在,不会报错
print('set2:',set2)
set2.pop()      #随机删除一个元素
#set.clear()         #会清空
#del实现删除
'''
intersection返回集合交集set1.intersection(set2)
union返回两个集合的并集
difference返回多个集合的差集'''
print("并集",set1|set2)        #并集
print("交集",set1&set2)       #交集
print('差集',set1-set2)       #差集

'''tuple:允许重复,里面的元素不能增删改,只能查
元组可以转换成字典,但是要符合格式,类似于('a',1),['b',3]这种'''
