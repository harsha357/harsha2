n,m=map(int,input().split())
b=list(map(int,input().split()))
for i in range(m):
  j,k=map(int,input().split())
  print(min(b[j-1:k]))
