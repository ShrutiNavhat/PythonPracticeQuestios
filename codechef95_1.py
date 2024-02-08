# cook your dish here
t=int(input())
for i in range(t):
    N=int(input())
    b=input()
    c1=0
    c2=0
    c3=0
    c4=0
    d=[]
    a="AB"
    j=0
    v=len(b)
    while j<v:
        if b[j]=="A B":
           c1=c1+1
        if b[j]=="A":
            c2=c2+1
        elif b[j]=="B":
            c3=c3+1
        elif b[j]=="O":
            c4=c4+1
        j=j+1
    print(c1, c2, c3, c4)
    if c2>=c3:
        print((c2-c3)+c3+c4+c1)
    elif c3>c2:
        print((c3-c2)+c2+c4+c1)
    else:
        print(c2+c3+c4+c1)
    
