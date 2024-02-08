t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    b=input()
    i=0
    c=0
    c1=0
    while i<n:
        if (a[i]=="R" and b[i]=="S") or (a[i]=="S" and b[i]=="P" ) or (a[i]=="P" and b[i]=="R"):
            c=c+1
        elif (b[i]=="R" and a[i]=="S") or (b[i]=="S" and a[i]=="P" ) or (b[i]=="P" and a[i]=="R"):
            c1=c1+1
        i=i+1
    if c>=c1:
        print(0)
    else:
        print(c1-c)
            
