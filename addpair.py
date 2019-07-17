b,c=map(int,input().split())
d=list(map(int,input().split()))[:b]
k=0
for i in range(b):
  for j in range(b):
    if(j>i):
      if(d[i]+d[j]==c):
        k=1
if(k>0):
  print("yes")
else:
  print("no")
