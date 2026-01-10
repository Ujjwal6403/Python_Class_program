# procedural
def checkEven(no):
   if(no % 2 == 0):
      return True
   else:
      return False

def main():
   value = 0
   ret = False
   print("Enter the number : ")
   value = int(input())

   ret =checkEven(value)
   print(ret)
   print(ret)
if __name__ == "__main__":
   main()