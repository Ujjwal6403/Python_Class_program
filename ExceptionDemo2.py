def main():
   Ans = 0
   
   
   try:
      print("Enter First number : ")
      No1 = int(input())
   
      print("Enter First number : ")
      No2 = int(input())
      print("inside try ")
      Ans = No1 / No2
      
   except:
      print("Inside except ")
      
   finally:
      print("Insider finally")
   
   print("Division is : ",Ans)
   
if __name__ == "__main__":
   main()