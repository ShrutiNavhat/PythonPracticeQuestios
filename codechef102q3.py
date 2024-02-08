t=int(input())
for i in range(t):
    n=int(input())
    k=int(input())
    i=1
    b=[]
    while i<=n:
        b.append(i)
        i=i+1
    j=0
    c=[]
    d=k-sum(b)
    f=b[-1]
    while j<n-1:
        if n>=k:
            print(-1)
        elif sum(b)==k:
            print(b)
        else:
            c.append(b[j])
            c.append(d+f)
        j=j+1
    print(c)
