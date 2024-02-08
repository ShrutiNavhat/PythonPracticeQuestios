i=1
a=int(input("enter the number :"))
while i==1:
    if a==2 or a==3 or a==5 or a==7:
        print(a,"it is prime number")
    elif a%2!=0 and  a%3!=0 and a%5!=0 and a%7!=0:
        print(a,"it is prime number")
    else:
        print(a,"it is not prime number")
    i=i+1

