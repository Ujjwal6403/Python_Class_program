def main():
   fobj = None
   try:
      fobj=open("Hello.txt","w")
      print("file get Succesfully opend")
      
      fobj.write("jay ganesh marvellous")
      
      fobj.close()
   except FileNotFoundError:
      print("Unable to open file as there is no such file")
   
   finally :
      print("End of aaplication ")
      
   
if __name__ == "__main__":
   main()