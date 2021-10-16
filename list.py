#使用者：姜海波
#创建时间：2021 / 1 / 18
#11: 32
lst1=['i','asg','asdl','b']
lst2=['sdv','efas','aeg']
lst1[1:1]=lst2
print(lst1)
lst3=lst1[1:3]
print(lst3,lst1)
lst1[3]=456
lst1[1:3]=[]
print(lst1)


#排序
lst4=[322,321,3445,345,340]
lst4.sort()
print(lst4)
lst4.sort(reverse=True)
print(lst4)
newlst4=sorted(lst4,reverse=True)
print(newlst4)

a=tuple(['fbio','bios','boier'])
print(a)