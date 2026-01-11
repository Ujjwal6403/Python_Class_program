no = 11            #globle
def fun():
   global no
   print("Value o no fun is : ",no)  # 11
   no = no + 1
   print("Value o no fun is : ",no)  # 12
   
print("Value of No is : ",no)   # 11
fun()
print("Value of No is : ",no)   # 12
   