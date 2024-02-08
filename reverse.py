t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    i=0
    b=[0]*n
    while i<n:
        b[i]=a[(n-1)-i] 
        i=i+1
    print(b)       
