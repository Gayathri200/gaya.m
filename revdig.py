f=int(input())
temp=0
while(f>0):
  r=f%10
  temp=(temp*10)+r
  f=int(f/10)
print(temp)
