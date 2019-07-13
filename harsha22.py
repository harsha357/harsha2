a=input()
b=list(map(int,input().split()))
c=False
for i in b:
    if b.count(i)>1:
      c=True
      break
if c:
  print(i)
else:
  print("unique")
