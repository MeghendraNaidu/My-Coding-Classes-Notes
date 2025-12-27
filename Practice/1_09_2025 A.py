class Calculator:
    def add(self, a, b):
        print(a + b)
        
    def sub(self, a, b):
        print(a - b)
        
    def mul(self, a, b):
        print(a * b)
        
    def div(self, a, b):
        print(a / b)
        if b != 0:
            print(a / b)
        else:
            print("Division By Zero Not Possible")
    
    def fdiv(self, a, b):
        print(a // b)
        if b != 0:
            print(a // b)
        else:
            print("Division By Zero Not Possible")
            
    def mod(self, a, b):
        print(a % b)
        if b != 0:
            print(a % b)
        else:
            print("Division By Zero Not Possible")
            
cal1 = Calculator()
cal2 = Calculator()

cal1.add(2, 4)
cal2.add(3, 5)

cal1.sub(2, 4)
cal2.sub(3, 5)

cal1.mul(2, 4)
cal2.mul(3, 5)

cal1.div(2, 4)
cal2.div(3, 5)

cal1.fdiv(2, 4)
cal2.fdiv(3, 5)

cal1.mod(2, 4)
cal2.mod(3, 5)