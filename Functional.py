addition = lambda A,B: A+B

Substraction = lambda A,B: A-B

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter First number : "))
No2 = int(input("Enter second number : "))

Ans = addition(No1 , No2)      # Ans = no1 + no2  -> ans = 11 + 10
print("Addition is : ",Ans)

Ans = Substraction(No1 , No2)   # ans = no1 - no2  -> ans = 11-10
print("Substaction is : ",Ans)
