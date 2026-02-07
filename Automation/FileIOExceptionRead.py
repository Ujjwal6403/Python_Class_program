def main():
   fobj = None
   try:
      fobj=open("Hello.txt","r")
      print("file get Succesfully opend")
      
      Data = fobj.read()
      print("Data from file is : ",Data)
      
      
      fobj.close()
   except FileNotFoundError:
      print("Unable to open file as there is no such file")
   
   finally :
      print("End of aaplication ")
      
   
if __name__ == "__main__":
   main()