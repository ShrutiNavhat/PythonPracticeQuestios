t=int(input())
for i in range(t):
    n,m=map(int, input().split())
    i=0
    while i<1:
        if n<=m:
            if (n-m)%2==0:
                print("yes")
            else:
                print("no")
        else:
            if (m-n)%2==0:
                print("yes")
            else:
                print("no")
        i=i+1
