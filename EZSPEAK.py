t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    b=["a","e","i","o","u"]
    i=0
    c=0
    d=0
    while i<n:
        if s[i]  in b:
            c=i
            break
        elif s[i]  not in b:
            d=i
        else:
            c=0
        i=i+1
    if c<5 and d<4:
        print("YES")
    else:
        print("NO")
        

