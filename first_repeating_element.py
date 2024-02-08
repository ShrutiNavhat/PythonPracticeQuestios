t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    i=0
    c1=0
    while i<n:
        j=i+1
        while j<n:
            if arr[i]==arr[j]:
               c1=c1+1
               if c1==1:
                  print(arr[i])
            j=j+1
        i=i+1
 
    
    
    

