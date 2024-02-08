t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    i=0
    b=[0]*n
    #b=[0,0,0,0,0,0,0]its taking 0 till n
    while i<n:
        b[i]=arr[n-i-1]
        i=i+1
    print(b)
        
        
