t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    i=0
    b=min(a)
    c=[]
    d=[]
    c1=0
    while i<n:
        if b==a[i]:
            c1=c1+1
            d.append(i)
        else:
            c.append(a[i])
        i=i+1
    f=(d[-1])
    j=0
    k=[]
    l=[]
    while j<n:
        if j==f:
            l.append(a[j])
        else:
            k.append(a[j])
        j=j+1
    print(sum(k))
