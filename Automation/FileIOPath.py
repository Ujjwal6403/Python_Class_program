import os

def main():
   FileName = input("Enter the name of file : ")
   Ret = os.path.isabs(FileName)
   
   if(Ret == True):
      print("It is absolute Path")
   
   else:
      print("It is relative Path")
   
      
if __name__ == "__main__":
   main()