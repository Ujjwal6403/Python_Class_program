import os

def main(): 
   FileName = input("Enter the name of file : ")     # Demo.txt
   
   if(os.path.exists(FileName)):
         
     fobj = open(FileName,"r")
     
     print(fobj.readable())
     print(fobj.writable())
     print(fobj.seekable())
     
     fobj.close()
     print(fobj.close)   # True
     
   else:
      print("There is no such file ")
      
if __name__ == "__main__":
   main()