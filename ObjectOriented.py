class arithematic :
   def addition(self,A,B):
      return A+B

   def Substraction(self,A,B):
      return A-B

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter First number : "))
No2 = int(input("Enter second number : "))

Ans = arithematic().addition(No1,No2)
print("Addition is. : ",Ans)

Ans = arithematic().Substraction(No1,No2)
print("Substaction is : ",Ans)

