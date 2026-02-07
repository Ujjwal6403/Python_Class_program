
# seek(kuthe, kuthun)
# Kuthun : 0 / 1 / 2
# 0 : Starting
# 1 : Current
# 2 : End

def main():
   fobj = None
   try:
      fobj=open("Hello.txt","r")
      print("file get Succesfully opend")
      
      print("current offset is : ",fobj.tell())    # 0
      
      fobj.seek(6,0)
      
      print("current offset is : ",fobj.tell())    # 11
      
      Data = fobj.read(6)
      
      print("current offset is : ",fobj.tell())   # 17
      
      print("Data from file is : ",Data)
      
      
      fobj.close()
   except FileNotFoundError:
      print("Unable to open file as there is no such file")
   
   finally :
      print("End of aaplication ")
      
   
if __name__ == "__main__":
   main()