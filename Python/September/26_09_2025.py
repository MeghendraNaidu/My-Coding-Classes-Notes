# Recursion Concept

#Recursion


# count = 0
# def example():
#     global count
#     if count >= 3:
#         return 
    
#     count += 1
#     print(count)
#     example()

# example()






def sample_function(n):
    if n <= 1:
        return 
    
    print(n)
    print(n)
    sample_function(n-1)
    print(n)
    


sample_function(10)




#Factorial of a number

#5 factorial => 120 => 5 * 24 
#4! => 4 * 6
#3! => 3 * 2
#2! => 2 * 1
#1! => directly return 1




def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)


print(fact(5))