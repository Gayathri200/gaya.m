x=int(input())
temp=0
while(x>0):
  n=x%10
  s=n**2
  temp=temp+s
  x=int(x/10)
print(temp)  
