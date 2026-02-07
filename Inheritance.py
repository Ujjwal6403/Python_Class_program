class parent:
   def __init__(self):
      print("Insider parent constructor")
      self.No1 = 10
      self.No2 = 20
      
   def fun(self):
      print("Inside Fun method of parent")
   
class Child(parent):
   def __init__(self):
         super().__init__()
         print("Inside child constructor")
         self.A = 11
         self.B = 21
      
   def sun(self):
         print("Inside sun method of child")
         
cobj = Child()