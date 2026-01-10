# Accept : Multiple parameter
# Return : Multiple value

def Marvellous1(value1,value2):
   print("Inside Marvellous1 : ",value1,value2)
   return 11,21,51
   
def main():
   Result1  = None
   Result2  = None
   Result3  = None
   
   Result1,Result2,Result3 =  Marvellous1("python",21)
   print("Return value is : ",Result1,Result2,Result3)

if __name__ =="__main__":
    main()
