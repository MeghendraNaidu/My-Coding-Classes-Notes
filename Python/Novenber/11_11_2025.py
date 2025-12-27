# All Exceptions are Errors but all errors are not Exceptions
# Exception means aa error while in runtime

# 4 Keywords
# try, except. else, finally

try:
    num1 = int(input("Enter Num1:"))
    num2 = int(input("Enter Num2:"))
    print(num1 / num2)
except:
    print("There is some isuues with code")
    
try:
    num1 = int(input("Enter Num1:"))
    num2 = int(input("Enter Num2:"))
    print(num1 / num2)
except Exception as e:
    print(e)
    print("There is some isuues with code")

try:
    num1 = int(input("Enter Num1:"))
    num2 = int(input("Enter Num2:"))
    print(num1 / num2)
except Exception as e:
    print(e)
    print("There is some isuues with code")
else:
    print("Division Succesfull")
finally:
    print("Thanks For Using This Application")
    
    
# First it Try to check the "Try" block code if it is executed it will go to the "else" and last it go to "Finally". 
# If "Try" execution is filled means it go to "except" block of code if it go to except block it does not go to the else block. 
# In "except"  for finding errors we use "Exception as e" for specifing an error use the "Error Name Code" Ex: Zero Dvision Error, 
# Value Error, KeyboardInterrupt etc. In that 4 keywords "Try" and "Finally" must should need to run. 
# If you write lot of except block it execute only one which is satisfied that condition.