a=list(map(int, input().split()))
b=int(input())
i=0
d=0
while i<len(a):
    if a[i]==b:
        d=d+1
    i=i+1
if d>=1:
    print("yes")
else:
    print("no")



x,n,m=map(int, input().split())
if (x+m)>=n:
    print("yes")
else:
    print("no")
    
    
    
s=input()
i=1
b=0
c=0
while i<len(s):
    if s[-i]=="1":
        b=b+c
    c=2**i
    i=i+1
print(b)
