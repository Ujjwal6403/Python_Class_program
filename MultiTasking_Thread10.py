import threading

def SumEven(No):
   sum = 0
   for i in range(2,No+1,2):
      sum = sum + i
   print("Even sum is : ",sum)
      
def Sumodd(No):
   sum = 0
   for i in range(1,No+1,2):
      sum = sum + i
      
   print("odd sum is : ",sum)
   
def main():
   SumEven(10000000)
   Sumodd(10000000)
   
  
   
if __name__ == "__main__":
   main()