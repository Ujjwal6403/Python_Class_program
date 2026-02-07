def main():
   try:
      open("Demo.txt","r")
      print("file get Succesfully opend")
      
   except FileNotFoundError:
      print("Unable to open file as there is no such file")
   
   finally :
      print("End of aaplication ")
if __name__ == "__main__":
   main()