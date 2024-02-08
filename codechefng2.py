t=int(input())
for i in range(t):
    N=int(input())
    a=list(map(int, input().split()))
    i=0
    c=[]
    b=0
    c1=0
    while i<N:
        if a[i]%2==0:
            c.append(i)
        i=i+1
    j=1
    k=0
    while j<len(c):
        if c[k]+1==c[j]:
            c1=c1+1
        k=k+1
        j=j+1
    if len(c)>0:
        print(c1+1)
    else:
        print(c1)
