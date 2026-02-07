import hashlib
import os
def CalculateCheckSum(FileName):
   fobj = open(FileName, "rb")
   
   hobj = hashlib.md5()
   
   Buffer = fobj.read(1000)
   while(len(Buffer) > 0):
      hobj.update(Buffer)
      
      Buffer = fobj.read(1000)

   fobj.close()
   
   return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
   Ret = False
   Ret = os.path.exists(DirectoryName)
   
   if(Ret == False):
      print("There is no such Directory")
      return
   Ret = os.path.isdir(DirectoryName)
   
   if(Ret == False):
      print("It is not a directory")
      return
   
   for FolderName, SubFolderName,FileName in os.walk(DirectoryName):
      for fname in FileName:
         fname = os.path.join(FolderName,fname)
         
         Checksum = CalculateCheckSum(fname)
         
         print(f"File Name : {fname} Checksum : {Checksum}")
   
def main():
   ret = CalculateCheckSum("Demo.txt")
   
   print("checkSum is : ",ret)
   
   
if __name__ == "__main__":
   main()
   