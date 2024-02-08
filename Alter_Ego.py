t=int(input())
for i in range(t):
    N=int(input())
    A=list(map(int, input().split()))
    i=1
    j=0
    b=[]
    c=[]
    d=[]
    while j<N:
        if A[j]>=A[i]:
            c.append(A[j])
            b.append((A[j]-A[i])//2)
        elif A[j]<A[i]:
            c.append(A[i])
            b.append((A[i]-A[j])//2)
        if A[j]<=A[i]:
            d.append(A[j])
        elif A[j]>A[i]:
            d.append(A[i])
        i=i+2
        j=j+2
    k=0
    f=[]
    g=0
    while k<len(b):
        if b[k]!=0:
            f.append(c[k]-b[k])
            f.append(b[k])
        else:
            g=(-1)
            break
        k=k+1
    g= sorted(f, reverse=True)
    print(g)

           
    
    
