t=int(input())
for i in range(t):
    a1,a2,a3,b1,b2,b3=map(int, input().split())
    a=[]
    a.append(a1)
    a.append(a2)
    a.append(a3)
    b=max(a)
    c=min(a)
    d=a1+a2+a3
    print(d)
    e=d-b-c
    print(e)
    print(b*100+e*10+c*1)
