import sys
def main():
   Border = "_"*40
   print(Border)
   print("--------- Marvellous Automation ---------")
   print(Border)
   
   if(len(sys.argv) == 2): 
      if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
         print("This application is used to perform _____")
         print("This is a automation script")
      elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
         print("Use the give script as")
         print("ScriptName.py Argument1 Argument2")
         print("Argument1 :__________")
         print("Argument2 :__________")
      
      else:
         print("Use the given flags as : ")
         print("--u : Used to display the usage")
         print("--h : Used to display the help")
         
   else:
      print("Invalid Number of command Line arguments")
      print("Use the given flags as : ")
      print("--u : Used to display the usage")
      print("--h : Used to display the help")
   
   print(Border)
   print("----- Thank you for using our srcipt-------")
   print("--------- Marvellous Automation -----------")
   print(Border)
                
if __name__ == "__main__":
   main()