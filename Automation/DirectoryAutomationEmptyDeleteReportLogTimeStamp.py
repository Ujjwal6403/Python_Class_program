import sys
import os
import time

def DirectoryScanner(DirName = "Marvellous"):
   Border = "-"*50
   timestamp = time.ctime()
   
   LogFilename = "Marvellous%s.log" %(timestamp)
   LogFilename = LogFilename.replace(" ","_")
      
   fobj.write(Border+"\n")
   fobj.write("This is a log File created by marvellous Automation")
   fobj.write("This is a directory cleaner script")
   
   Ret = False
   
   Ret = os.path.exists(DirName)
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
    
         if(os.path.getsize(fname) == 0):
            EmptyFileCount = EmptyFileCount + 1
            os.remove(fname)
            
   fobj.write("Total files scanned : "+str(FileCount)+"\n")
   fobj.write("Total empty files found : "+str(EmptyFileCount)+"\n")
   fobj.write("This log file is created at : "+timestamp+"\n")
   fobj.write(Border+"\n")
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