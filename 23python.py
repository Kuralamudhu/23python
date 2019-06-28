z=int(input())
p=0
h=z
while h>0:
  digit = h%10
  p += digit **3
  h //=10
if z==p:
  print("yes")
else:
  print("no")
