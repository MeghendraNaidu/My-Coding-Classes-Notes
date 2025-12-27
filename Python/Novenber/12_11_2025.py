# we can write our own exception class using Inheritance

# Iterators and Generators
# Iterable and Iterators are not same 
# Iterable means iterating every element in a list

# Iterators
# There are 2 main function : iter(), next()

list1 = [1, 5, 7, 9, 11, 13]
itr1 = iter(list1)
# print(next(itr1))
# print("Very Random Task")
# print(next(itr1))
# print(next(itr1))
# print(next(itr1))
# print(next(itr1))
# print(next(itr1))
# print(next(itr1)) # for this we will get an  "Stop Iteration" Exception Error
# Because we are calling more items then the list of items

str1 = "Good AfterNoon"


# Even Numbers
# We can write Our Own Custom Iterators

class EvenIterator():
    
    def __init__(self, limit):
        self.curr_value = 0
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr_value > self.limit:
            raise StopIteration
        
        temp = self.curr_value
        self.curr_value += 2
        return temp

eitr1 = EvenIterator(10)
# print(next(eitr1))
# print(next(eitr1))
# print(next(eitr1))
# print(next(eitr1))
# print(next(eitr1))
# print(next(eitr1))

# RangeIterator
# low 5
# upper 15

class RangeIterator():
    
    def __init__(self, lower_bound, upper_bound):
        self.curr_value = lower_bound
        self.upper_bound = upper_bound
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr_value > self.upper_bound:
            raise StopIteration
        
        temp = self.curr_value
        self.curr_value += 1
        return temp 
    
ran1 = RangeIterator(5, 15)
# print(next(ran1))
# print(next(ran1))

class RangeIterator1():
    
    def __init__(self, lower_bound, upper_bound):
        self.curr_value = lower_bound
        self.upper_bound = upper_bound
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr_value < self.upper_bound:
            raise StopIteration
        
        temp = self.curr_value
        self.curr_value -= 1
        return temp
ranf3 = RangeIterator1(15, 5)
# print(next(ranf3))
# print(next(ranf3))

# Generators 

def gen1():
    yield 1
    print("hi")
    yield 2
    yield 4
    yield 5
# var1 = gen1()
# print(next(var1))
# print(next(var1))
# print(next(var1))
# print(next(var1))

# EvenIterator => Without any limit

def gen2(limit):
    
    curr_value = 0
    while True:
        if curr_value > limit:
            break
        
        yield curr_value
        curr_value += 2
var1 = gen2(10)
# print(next(var1))
# print(next(var1))
# print(next(var1))
# print(next(var1))
# print(next(var1))
# print(next(var1))
# print(next(var1))

# Fibanocii Generator
def fibgen():
    num1, num2 = 0, 1
    while True:
        yield num1
        # temp = num1 + num2
        # num1 = num2
        # num2 = temp
        num1, num2 = num2, num1 + num2
var2 = fibgen()
# print(next(var2))
# print(next(var2))
# print(next(var2))
# print(next(var2))

list1 = [num1 for num1 in range(0, 100, 2)]
list1 = [num1 * 2 for num1 in range(0, 100, 2)]
gen1 = (num1 * 2 for num1 in range(0, 100, 2))

# print(next(gen1))
# print(next(gen1))