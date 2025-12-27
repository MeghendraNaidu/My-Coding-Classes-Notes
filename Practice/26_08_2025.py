# {0:"even",1:"odd",2:"even",3:"odd",4:"even",5:"odd"}

n = 10
print(dict((i, "Even" if i % 2 == 0 else "Odd") for i in range(0, n + 1)))