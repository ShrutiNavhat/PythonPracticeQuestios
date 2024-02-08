n=int(input())
s=input()
i=0
c=0
b=0
c1=0
while i<n:
  b=i+1
  c=b+1
  if s[i]=="A" and s[b]=="B" and s[c]=="C":
    print(i)
  i=i+1
