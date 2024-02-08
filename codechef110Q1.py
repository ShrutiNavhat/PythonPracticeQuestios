t=int(input())
for i in range(t):
    A,B=map(int, input().split())
    i=0
    d=max(A,B)
    e=min(A,B)
    c=0
    while i<d:
        if A%B!=0:
            A=A+1
            B=B-1
            c=c+1
        else:
            c=c+0
            break
        i=i+1
    print(c)
