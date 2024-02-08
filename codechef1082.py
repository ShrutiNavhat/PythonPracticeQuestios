t=int(input())
for i in range(t):
    N,X=map(int, input().split())
    if N==X or X==0:
        print((N-X)//2)
    elif X>=N*2 and X%2!=0:
        print((X//2)+1)
    elif X>=N*2 and X%2==0:
        print(X)
    else:
        print(((N*2)-X)//2+(X//2))
    
