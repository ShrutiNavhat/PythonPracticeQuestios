t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int, input().split()))
    i=0
    j=0
    c=max(p)
    d=min(p)
    f=0
    g=0
    while i<n:
        if c==p[i]:
            f=i
            
        elif d==p[i]:
           
            g=i
        i=i+1
        j=j+1
    if g<f:
        print(g+((n-1)-f))
    else:
        print(g+((n-1)-f)-1)
    
    https://www.codechef.com/problems/DARLIG
https://www.codechef.com/problems/ELEVSTRS
https://www.codechef.com/problems/XLSQUARE
    
    
    
    
