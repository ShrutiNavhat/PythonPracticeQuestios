t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    i=0
    b=[]
    while i<n:
        j=i+1
        while j<n:
            b.append(a[i]*a[j])
            j=j+1
        i=i+1
    print(sum(b))
