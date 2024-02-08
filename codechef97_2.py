t=int(input())
for i in range(t):
    A1,A2,A3,B1,B2,B3=map(int, input().split())
    b=[]
    b.append(A1)
    b.append(A2)
    b.append(A3)
    c=[]
    c.append(B1)
    c.append(B2)
    c.append(B3)
    h=[]
    g=[]
    j=0
    m=0
    i=0
    while i<3:
        if b[i]>j:
            j=b[i]
        if c[i]>m:
            m=c[i]
        i=i+1
    k=0
    n=0
    l=0
    while k<3:
        if b[k]>n and b[k]!=j:
            n=b[k]
        if c[k]>l and c[k]!=m:
            l=c[k]
        k=k+1
    if (n+j)>(m+l):
        print("Alice")
    elif (n+j)<(m+l):
        print("Bob")
    else:
        print("Tie")
    
