t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    i=0
    c=[0]*n
    while i<n:
        c[i]=(i+1)
        j=0
        while j<n:
            if c[j]!=a[i]:
                print(c[j])
            j=j+1
        i=i+1
    
   
