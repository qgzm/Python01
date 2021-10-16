stream=open('data.txt','w')
s='''hwie
dsoah
djofe'''
a=stream.write(s)
print(a)
stream.close()

m=open(r'data.txt','rb')
a=m.read()
n=open(r'演练\data.txt','ab')
n.write(a)

m.close()
n.close()