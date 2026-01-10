
def EmployeeInfo(name , age , salary, city = "Pune"):
   print("Name : ",name)
   print("Age : ",age)
   print("Salary : ",salary)
   print("City : ",city)
   
def main():
   EmployeeInfo("Rahul",26,2000)
   EmployeeInfo("Rahul",26,2000,"MUmbai")
if __name__== "__main__":
   main()