a=list(map(int, input().split()))
i=0
b=a[i]
while i<len(a):
    if b>a[i]:
        b=i
    i=i+1
print(b)
   
            
