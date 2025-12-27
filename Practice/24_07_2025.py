units = float(input("Enter your units : "))
if units >= 500:
    print(f'price: {units * 3 + 50}')
elif 300 > units >= 200:
    print(f'price: {units * 3}')
elif 200 > units >= 100:
    print(f'price: {units * 2}')
else:
    print(f'price: {units * 1}')