#f=open('demo','r')
#print(f.read())
#f.close()
#f.close()

#t=open('demo','w')
#t.write('simar\n')
#t.close()

#x=open('demo','a')
#x.write('raman')

#t=open('demo','w+')
#t.write('taran')
#print(t.read())

#t=open('demo','r')
#print(t.read(4))
#t.seek(0)
#print(t.read(5))

#t=open('demo','a+')
#t.write('hello')
#print(t.read())

#t=open('demo','w')
#t.writelines(['taran\n','raman\n','simar\n'])

t=open('demo','r')
l=t.readlines()
print(l)
for x in l:
    print(x)