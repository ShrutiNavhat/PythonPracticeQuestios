t=int(input())
for i in range(t):  
    arr=list(map(int, input().split()))
    s=int(input())
    i=0
    k=1
    while i<len(arr):
        j=k
        while j<len(arr):
            if arr[i]+arr[j]==s:
                print(arr[i],arr[j])
            j=j+1
        i=i+1
        k=k+1
    
    

