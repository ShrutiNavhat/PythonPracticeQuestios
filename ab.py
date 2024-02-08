N=int(input())
S=input()
i=1
j=0
c=0
while i<N:
  if (S[j]=="a" and S[i]=="b") or (S[j]=="b" and S[i]=="a"):
    c=c+1
  i=i+1
  j=j+1
if c>=1:
  print("Yes")
else:
  print("No")

