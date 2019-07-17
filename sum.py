f,g=map(int,input().split())
b=list(map(int,input().split()))
for i in range(g):
  j,k=map(int,input().split())
  print(sum(b[j-1:k]))
