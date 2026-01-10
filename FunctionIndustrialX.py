# procedural
def checkEven(no):
   if(no % 2 == 0):
      return True
   else:
      return False

def main():
   value = 0
   Ret = False
   print("Enter the number : ")
   value = int(input())

   Ret =checkEven(value)
   
   if(Ret == True):
      print("It is Even")
   else:
      print("It is odd")
      
if __name__ == "__main__":
   main()