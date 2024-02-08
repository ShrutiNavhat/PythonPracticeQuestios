t=int(input())
for i in range(t):  
    arr=list(map(int, input().split()))
    i=0
    c1=0
    c=[0]*len(arr)
    b=[0]*len(arr)
    while i<len(arr):
        j=i+1
        while j<len(arr):
            if arr[i]==arr[j]:
                c[i]=arr[i]
                c1=c1+1
                break
            else:
                b[i]=arr[i]
                break
            j=j+1
        i=i+1
    k=0
    l=0
    while k<len(b)-1:
        if arr[k]==arr[-1]:
            l=0
            break
        elif arr[k]!=arr[-1]:
            l=arr[-1]
        k=k+1
    b[-1]=l
    print(b)
        
        
#t=int(input())
#for i in range(t):  
    #arr=list(map(int, input().split()))
    #i=0
    #k=0
    #c=[0]*len(arr)
    #b=[0]*len(arr)
    #while i<len(arr):
     #   j=k+1
      #  while j<len(arr):
       #     if arr[i]==arr[j]:
        #        c[i]=arr[i]
         #       break
         #   else:
          #      b[i]=arr[i]
           # j=j+1
        #i=i+1
        #k=k+1
    #print(c)
    #print(b)
