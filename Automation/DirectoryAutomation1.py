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
   
   for FolderName , FubFolder ,FileName in os.walk(DirName):
      for fname in FileName:
         print(fname)
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
if __name__ == "__main__":
   main()