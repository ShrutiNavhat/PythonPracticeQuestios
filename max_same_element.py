
         
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    i=0
    k=0
    c1=0
    while i<n:
        j=k+1
        while j<n:
            if arr[i]==arr[j]:
                print(arr[i])
                c1=c1+1
                break
            j=j+1
        k=k+1
        i=i+1
