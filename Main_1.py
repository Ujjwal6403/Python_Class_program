
def Multiplication(value1,value2):
   ans = 0
   ans = value1 * value2
   return ans
def main():
   No1 = 0
   No2 = 0
   Result = 0

   No1 = int(input("Enter First Number " ))
   No2 = int(input("Enter Second Number " ))


   Result = Multiplication(No1,No2)
   print("Multiplication is : ",Result)
   
main()