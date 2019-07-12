f=int(input())
g=map(int,input().split())
h=sorted(g)
h.reverse()
if(h[0]==0):
  print("0")
else:
  for i in h:
   print(i,end='')
