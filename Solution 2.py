c=eval(input())
c=[str(i) for i in t]
c.sort()
b=''
for i in range(len(t)-1):
    if c[i][0]==c[i+1][0] and len(c[i])<len(c[i+1]):
        a=c[i]
        c[i]=c[i+1]
        c[i+1]=a
for i in range(len(c)-1,-1,-1):
    b=b+c[i]
print(int(b))
