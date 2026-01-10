
def EmployeeInfo(name, age, salary, city):
   print("Name : ",name)
   print("Age : ",age)
   print("Salary : ",salary)
   print("City : ",city)
   
def main():
   #Positional 
   # EmployeeInfo("Rahul",26,25000.50,"pune")  # Correct
   # EmployeeInfo(26,"Rahul","pune",20000.50)  # wrong
   
   # Keyword arguments
   EmployeeInfo(age = 26,name = "Rahul",city = "pune",salary=2000.50)  # Correct
   
   
if __name__== "__main__":
   main()