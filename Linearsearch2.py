t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=int(input())
    i=0
    c=0
    while i<n:
        if a[i]==b:
            c=c+1
        i=i+1
    if c>=1:
        print("yes")
    else:
        print("no")
