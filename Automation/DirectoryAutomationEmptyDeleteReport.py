import sys
import os
def DirectoryScanner(DirName = "Marvellous"):
   Ret = False
   
   Ret = os.path.exits(DirName)
   if(Ret == False):
      print("There is no such directory")
      return
   
   ret = os.path.isdir(DirName)
   if(Ret == False):
      print("it is not a directory ")
      return 
   
   FileCount = 0
   EmptyFileCount = 0
   
   for FolderName , FubFolder ,FileName in os.walk(DirName):
      
      for fname in FileName:
         FileCount = FileCount + 1
         
         fname = os.path.join(FolderName,fname)
         print("File Name : ",fname)
         print("File size : ",os.path.getsize(fname))   #Path issue
         if(os.path.getsize(fname) == 0):
            EmptyFileCount = EmptyFileCount + 1
            os.remove(fname)
   Border = "-"*50
   print(Border)
   print("------- Automation Report--------")
   print("Total Files Scanned : ", FileCount )
   print("Total empty files found :",EmptyFileCount)
   
   
   
def main():
   Border = "-"*50
   print(Border)
   print("---------marvellous Directory Automation----------")
   print(Border)
   
   if(len(sys.argv) != 2):
      print("Invalid nummber of arguments")
      print("Please specify the name of directory")
      return 
   DirectoryScanner(sys.argv[1])
   
   Border = "-"*50
   print(Border)
   print("---------marvellous Directory Automation----------")
   print(Border)
   
if __name__ == "__main__":
   main()