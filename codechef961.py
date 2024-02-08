t=int(input())
for i in range(t):
    N,m,k=map(int, input().split())
    a=list(map(int, input().split()))
    i=1
    j=0
    c=0
    while i<N:
        if a[i]-a[j]:
            c=c+a[i]-a[j]
        i=i+1
        j=j+1
    if (m//k)<=c:
        print("yes")
    else:
        print("no")
