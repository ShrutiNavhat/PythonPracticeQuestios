t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    b=sum(a)
    c=n*k
    d=b-c
    f=0
    if n%2==0:
        f=n//2
    else:
        f=(n//2)+1
    if  b==n and k>=1:
        print("yes")
    elif d//k and f==(d//k):
        print("yes")
        
    else:
        print("no")
