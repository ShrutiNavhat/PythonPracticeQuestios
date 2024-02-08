# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    i=0
    c=0
    c1=0
    c2=0
    d=[]
    d1=[]
    d2=[]
    c3=0
    while i<n:
         if a[i]==b[i]:
            c2=c2+1
            d.append(a[i]-b[i])
         elif a[i]>=b[i]:
            d1.append(a[i]-b[i])
            c=c+1
         else: 
            d2.append(b[i]-a[i])
            c1=c1+1
         i=i+1
    j=0
    while j<len(d1):
    if d2 in d1:
        c3=c3+1
        if n==c3:
            print("Draw")
    elif c+c2<c1+c2:
        print("Om")
    else:
        print("Addy")
        
        
        
# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    i=0
    c=0
    c1=0
    c2=0
    d=0
    d1=0
    d2=0
    while i<n:
         if a[i]==b[i]:
            c2=c2+1
            d=(a[i]-b[i])
         elif a[i]>=b[i]and  a[i]!=0:
            d1=(a[i]-b[i])
            c=c+1
         elif a[i]<=b[i] and b[i]!=0 : 
            d2=(b[i]-a[i])
            c1=c1+1
         i=i+1
    if d1==d2:
        print("Draw")
    elif c+c2<c1+c2:
        print("Om")
    else:
        print("Addy")
