n,k=map(int,input().split())
a=input()
w=a.replace(" ","")
s=len(w)
temp=0
if(s==n):
  while(0<k):
    k=k-1
    t=int(w[k])
    temp=temp+t
  print(temp)  
