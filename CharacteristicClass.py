import gc

class Demo:
   
   # class variable
   No1 = 10
   No2 = 11
   
   def __init__(self):
      print("Insider constructor")
      
   def __del__(self):
      print("Inside destructor")
      
print(Demo.No1)
print(Demo.No2)