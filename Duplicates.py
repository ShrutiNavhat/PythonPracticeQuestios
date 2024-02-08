t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    i=0
    k=0
    c1=0
    c=[0]*n
    while i<n:
        j=k+1
        while j<n:
            if arr[i]!=arr[j]:
               c1=c1+1
               c[i]=arr[i]
            j=j+1
            print(c1)
            print(c)
        c1=0
        i=i+1
        k=k+1
    
 
    
