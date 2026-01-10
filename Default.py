
def EmployeeInfo(name = "Gotya", age = 21, salary = 1000, city = "Pune"):
   print("Name : ",name)
   print("Age : ",age)
   print("Salary : ",salary)
   print("City : ",city)
   
def main():
   
  # EmployeeInfo(age = 26,name = "Rahul",city = "pune",salary=None)  # Correct
   EmployeeInfo()
if __name__== "__main__":
   main()