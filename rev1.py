m,n=map(str,input().split())
w=m.replace(" ","")
a=len(m)
i=int(n)
x=a-i
for i in range(x,a):
  print(w[i],end="")
for i in range(0,x):
  print(w[i],end="")  
