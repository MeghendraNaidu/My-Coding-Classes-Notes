import re


mobile_num_pattern = r"^[7-8]{1}[0-9]{9}$"
ip = "7465037927"
op = re.match(mobile_num_pattern, ip)
print(op)

# Username can contains LC, UC, Digits, _ and length
# should be in between 8 and 15

username_pattern = r"^[A-Za-z0-9_\.]{8,15}$"
ip = "James.999"
op = re.match(username_pattern, ip)
print(op)

# ? questin mark contain atleast once in a pattern

# Strong Password

password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9@._]{9,12}$"

# (?=.*[A-Z]) = assure atleast one uppercase in string
# (?=.*[a-z]) = assure atleast one lowercase in string
# (?=.*[0-9]) = assure atleast one digit in string

pswd = "INDIAhello2"
pop = re.match(password_pattern, pswd)
print(pop)



# Sir Notes


# mobile_num_pattern=r"^[7-8]{1}[0-9]{9}$"
# ip="7524179623"
# op=re.match(mobile_num_pattern,ip)
# print(op)


#username can contains LC,UC,Digits,_ and length
#  should be in b/w 8 and 15

# username_pattern=r"^[A-Za-z0-9_\.]{8,15}$"
# ip="James.999"
# op=re.match(username_pattern,ip)
# print(op)


#strong password.

password_pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9@._]{9,12}$"

# # (?=.*[A-Z]) --->assure atleast one uppercase in string 
# # (?=.*[a-z])--->assure atleast one lowercase in string
# # (?=.*[0-9])--->assure atleast one digit in string
# pswd="INDIAhello2"
# pop=re.match(password_pattern,pswd)
# print(pop)

# email1="harish.tech@gmail." 
# email2="akhil123.tech@yahoo.in" 
# email3="_kiran.mgr@10000coders.in" 

# 1.pattern before @
# 2.pattern after @ 
# 3.pattern for domain name before and after .

# email_pattern=r"^[A-Za-z0-9._]+@[A-Za-z0-9]+\.[a-zA-Z]{2,}$"
# op=re.match(email_pattern,email1)
# print(op)