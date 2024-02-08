t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    i=0
    s=0
    c=0
    f=0
    g=0
    while i<n:
        s=s+a[i]
        c=c+1
        if s/c>=f:
           f=s/c
           g=i
        i=i+1
    print(g)
  
    
        
