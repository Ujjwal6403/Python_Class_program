class parent:
   def __init__(self):
      print("Insider parent constructor")
     
      
   def fun(self):
      print("Inside Fun method of parent")
   
class Child(parent):
   def __init__(self):
         super().__init__()
         print("Inside child constructor")
 
   def fun(self):
         super().fun()
         print("Inside fun method of child")
         
cobj = Child()

cobj.fun()
