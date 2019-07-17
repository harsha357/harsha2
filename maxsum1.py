fg=int(input())
gh=list(map(int,input().split()))
cm=b[1:fg:2]
dm=b[0:fg:2]
if(sum(cm)>=sum(dm)):
  print(sum(cm))
else:
  print(sum(dm))
