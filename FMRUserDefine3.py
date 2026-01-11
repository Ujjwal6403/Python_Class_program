
CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No+1
Add = lambda A,B : A+B

def filterX(Task,Elements):
   Result = list()
   
   for no in Elements:
      Ret = Task(no)
      
      if(Ret == True):
         Result.append(no)
         
   return Result

def mapX(Task,Elements):
   Result = list()
   
   for no in Elements:
      Ret = Task(No)
      Result.append(Ret)
   return Result

def reduceX(Task,Elements):
   sum = 0
   
   # [11, 21, 23,31]
   for no in Elements:
      sum = Task(sum,no)
   return sum

def main():
   Data = [11,10,15,20,22,27,30]
   print("Actual data is : ",Data)
   
   FData = list(filterX(CheckEven,Data))
   
   print("Data after fileter is : ",FData)
   
   MData = list(map(Increment,FData))
   print("Data after map is : ",MData)
   
   RData = reduceX(Add,MData)
   print("Data after reduce is : ",RData)
   
if __name__ == "__main__":
   main()