# cook your dish here
t=int(input())
for i in range(t):
    N=int(input())
    a=list(map(int, input().split()))
    i=0
    c=[]
    c1=0
    c2=0
    while i<N:
            if a[i] not in c:
                c.append(a[i])
                c1=c1+1
            else:
                c2=c2+1
            i=i+1
    if c1==c2:
        print(c1)
    elif c2>1 and N%2!=0:
         print(c1)
    else:
         print(c1-c2)
        
        
   
            
