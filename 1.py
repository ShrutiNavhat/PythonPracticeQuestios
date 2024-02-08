# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int, input().split())
    i=0
    k=n
    l=m
    while i<=(n+m):
        if n==m:
            print("yes")
            break
        elif n>m:
            if (n-1)==(m+1):
              print("yes")
              break
            else:
              print("no")
              break
        elif n<m:
            if (n+3)==(m-1):
              print("yes")
              break
            else:
              print("no")
              break
        i=i+1
    
    
    
  
