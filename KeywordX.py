
def EmployeeInfo(name, age, salary, city):
   print("Name : ",name)
   print("Age : ",age)
   print("Salary : ",salary)
   print("City : ",city)
   
def main():
   # Keyword arguments
   EmployeeInfo(age = 26,name = "Rahul",city = "pune",salary=None)  # Correct
   
   
if __name__== "__main__":
   main()