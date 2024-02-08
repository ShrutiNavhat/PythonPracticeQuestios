t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    n1=int(input())
    arr1=list(map(int, input().split()))
    i=0
    c1=0
    while i<n:
        j=0
        while j<n1:
             if arr[i]==arr1[j]:
                c1=c1+1
             j=j+1
        i=i+1
    print(c1)
    if c1==n1:
       print("yes")
    else:
        print("no")
        
