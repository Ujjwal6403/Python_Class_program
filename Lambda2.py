
# Functional


# def checkEven(no):
   # return(no % 2 == 0)
   
checkEven =  lambda no : (no % 2 == 0)
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