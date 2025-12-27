# Adding Variables Using Constructor

# class Calculator:
    
#     def __init__(self, id1, manf_date1, mrp1):
#         self.id = id1
#         self.manf_date = manf_date1
#         self.mrp = mrp1
#         print("An Object is Created")
    
#     def add(self, a, b):
#         print(a + b)
#         print(self.id)
    
#     def describe(self):
#         print(self.id, self.manf_date, self.mrp)
        
# # id, manf_data, mrp
        
# clc1 = Calculator(1, "02-Sept", 200)
# clc2 = Calculator(2, "03-Sept", 300)
# # clc3 = Calculator()
# # clc4 = Calculator()

# clc1.describe()
# clc2.describe()

# print(clc1.id)


# Types of Variables => 1. Instance Variable, Static/Class Variable
# Typrs of Methods => 1. Instance methods, Static methods, Class methods

# Instance Variable => Those varialbe whose value is dependent on a Instance
# Static/Class Variable => These variable value is not dependent on an instance.
# It's value is common to all the objects of that class

# class Calculator:
#     company_name = "CASIO"
#     company_gst_number = "123456"
    
#     def __init__(self, id1, manf_date1, mrp1):
#         self.id = id1
#         self.manf_date = manf_date1
#         self.mrp = mrp1
#         print("An Object is Created")
    
#     def add(self, a, b): # Instead of "self" we can use any name
#         print(a + b)
#         print(self.id)
    
#     def describe(self):
#         print(self.id, self.manf_date, self.mrp)
        
#     @classmethod
#     def change_company_name(cls, new_name): # Instead "cls" we can use any name
#         cls.company_name = new_name
        
#     @staticmethod
#     def connect_to_db(db_password, db_username):
#         num1 = 10
#         print("Connecting to database.....")
    

# clc1 = Calculator()
# clc2 = Calculator()

# print(clc2.company_name)
# print(clc1.company_gst_number)
# print(Calculator.company_name)
    
# Types of Methods
# Instance Method

# classmethod
# staticmethod


class Calculator:
    company_name = "CASIO"
    company_gst_number = "123456"
    
    def __init__(self, id1, manf_date1, mrp1):
        self.id = id1
        self.manf_date = manf_date1
        self.mrp = mrp1
        print("An Object is Created")
    
    # def add(self, a, b): # Instead of "self" we can use any name
    #     print(a + b)
    #     print(self.id)
    
    def describe(self):
        print(Calculator.company_name)
        print(self.id, self.manf_date, self.mrp)
        
    @classmethod
    def change_company_name(cls, new_name): # Instead "cls" we can use any name
        cls.company_name = new_name
        
    @staticmethod
    def connect_to_db(db_password, db_username):
        num1 = 10
        print("Connecting to database.....")

clc1 = Calculator(2, "02-Sept", 400)
clc4 = Calculator(1, "02-Sept", 200)

clc4.describe()
# Calculator.describe()
Calculator.change_company_name("New Casio")
print(Calculator.company_name)
clc1.change_company_name("New New Casio")

# Static Methods
clc1.connect_to_db(1, 2)
Calculator.connect_to_db(2, 3)

Calculator.describe(clc1)