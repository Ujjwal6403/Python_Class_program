import gc

class Demo:
   
   def __init__(self):
      print("Insider constructor")
      
   def __del__(self):
      print("Inside destructor")
      
# Allocate
obj = Demo()

# Use


#Deallocate
del obj

gc.collect()

print("End of application")