t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    s=0
    s1=0
    i=0
    j=0
    k=(n-1)
    b=[]
    while i<n:
        c1=2**k
        b.append(c1)
        s1=max(b)
        s=sum(b)
        i=i+1
        k=k-1
    print(b)
    print(s-s1)
