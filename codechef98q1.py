# cook your dish here
t=int(input())
for i in range(t):
    X,Y,Z=map(int, input().split())
    if ((X*Y)%Z)==0:
        print((X*Y),Z)
    elif ((X*Z)%Y)==0:
        print((X*Z),Y)
    elif ((Y*Z)%X)==0:
        print((Y*Z),X)
    else:
        print(-1)
