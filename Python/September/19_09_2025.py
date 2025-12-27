# Time And Space Complexity

# Sum of n natural numbers
# Linear Time Complexity Codes
# O(n) Codes
n = 10
sum = 0

for i in range(1, n + 1): # 10 arthematic operations
    sum += i
print(sum)

# Method 2
# Constant Time Complexity codes
# O(1)
print((n * (n + 1) // 2)) # 3 arthematic operations


# No Of Operations ~~ Time
# O(1)
# O(n square)
# O(n cube)

m = 10
n = 20

for i in range(1, m + 1):
    for j in range(1, n + 1):
        print(i + j)
# O(m * n)

# if m == n 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j)


# O(logn) => O(logn) is present in between constant and linear
# O(nlogn) => O(nlogn) id present in between linear and n square
# And it continuosly go on

#  O(n square)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j)

#  O(n square)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j)

# O(n)   
for k in range(1, n + 1):
    print(k ** k)

print(2 + 3) # 1 unit time
# O(n square + n + 1) = O(n square)
# O(2n square + n + 1) = O(n square)


# Space Complexity

# Constant Memory 
n = 10
sum = 0 # 32 bits

for i in range(1, n + 1): 
    sum += i
print(sum)


# O(n) space complexity => worst case
# O(1) space complexity => Best case


