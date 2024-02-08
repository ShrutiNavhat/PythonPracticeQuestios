a=[1,2,3,5,8,2]
n=int(input())
i=0
b=len(a)
while i<b:
    if n==a[i]:
        print("yes")
        break
    elif n!=a[i] and i==(b-1):
        print("no")
    i=i+1
 
  
    
