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

def FindDuplicate(DirectoryName = "Marvellous"):
   Ret = False
   Ret = os.path.exists(DirectoryName)
   
   if(Ret == False):
      print("There is no such Directory")
      return
   Ret = os.path.isdir(DirectoryName)
   
   if(Ret == False):
      print("It is not a directory")
      return
   
   Duplicate = {}
   
   for FolderName, SubFolderName,FileName in os.walk(DirectoryName):
      for fname in FileName:
         fname = os.path.join(FolderName,fname)
         
         Checksum = CalculateCheckSum(fname)
         
         if Checksum in Duplicate:
            Duplicate[Checksum].append(fname)
         else:
            Duplicate[Checksum] = [fname]
            
   return Duplicate
def DisplayResult(MyDict):
   Result = list(filter(lambda x : len(x) > 1,MyDict.vaues()))
   
   count = 0
   
   for value in Result:
      for subvalue in value:
         count = count + 1
         print(subvalue)
      print("Value of count is : ",count)
      count = 0

def DeleteDuplicate(Path = "Marvellous"):
   Result = list(filter(lambda x : len(x) > 1,MyDict.vaues()))
   
   count = 0
   cnt  = 0
   for value in Result:
      for subvalue in value:
         count = count + 1
         if(count > 1):
            print("Deleted File : ",subvalue)
            os.remove(subvalue)
            cnt = cnt + 1
            
      count = 0
   
   print("Total deleted Files : ",cnt)
     
   
   MyDict = FindDuplicate(Path)
def main():
   ret = FindDuplicate()
   DisplayResult(ret)
   
   print("checkSum is : ",ret)
   
   
if __name__ == "__main__":
   main()
   