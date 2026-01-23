def main():
   Ans = 0
   try:
      print("Enter First number : ")
      No1 = int(input())
   
      print("Enter First number : ")
      No2 = int(input())
      print("inside try ")
      Ans = No1 / No2
      
   except ZeroDivisionError as zobj:
      print("Insder except : ",zobj)
      
   except ValueError as vobj:
      print("Inside except ",vobj)
      
      
   except Exception as eobj:       # generic except block
      print("Inside except : ",eobj)
      
   finally:
      print("Insider finally")
   
   print("Division is : ",Ans)
   
if __name__ == "__main__":
   main()