a=int(input())
lst=[]
for i in range(a):
  lst.extend(map(int,input().split()))
print(*sorted(lst))
