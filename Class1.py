class Demo:
   def __init__(self):
      print("Insider constructor")
      
   def __del__(self):
      print("Inside destructor")
      

obj = Demo()

print("End of application")