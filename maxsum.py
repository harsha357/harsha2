fg=int(input())
gh=list(map(int,input().split()))
c=b[1:fg:2]
d=b[0:fg:2]
if(sum(c)>=sum(d)):
  print(sum(c))
else:
  print(sum(d))
