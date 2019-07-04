x,y=map(str,input().split())
if len(x)!=len(y):
  print("no")
z=[x.count(i) for i in x]
w=[y.count(i) for i in y]
if(z==w):
  print("yes")
else:
  print("no")
