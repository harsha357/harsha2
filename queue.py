class Queue:
  def __init__(self,size=0):
    self.size=size
    self.list1=[]
  def add(self,data):
    if len(self.list1)>=self.size:
      print("queue is full")
      return
    self.list1.append(data)
  def remove(self):
    if len(self.list1)<=0:
      print("queue is empty")
      return
    data=self.list1.pop(0)
    return data
  def printQueue(self):
    for ele in self.list1:
      print(ele)
obj=Queue(5)
obj.add([10,100,20])
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.remove()
obj.printQueue()
