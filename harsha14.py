pri=int(input())
if(pri>1):
  for i in range(2,pri):
    if(pri%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
