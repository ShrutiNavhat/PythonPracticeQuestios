a=[3,2,5,6,0,3,1]
l=len(a)
for i in range(l-1):

    index=i;
    for j in range(i+1,l):
        if a[index]>a[j]:
            index=j
        
    b=a[i]
    a[i]=a[index]
    a[index]=b
       
print(a)
    
    
    
a=list(map(int, input().split()))
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]>a[j]:
            b=a[i]
            a[i]=a[j]
            a[j]=b
        j+=1
    i+=1
print(a)                                                                                                  
